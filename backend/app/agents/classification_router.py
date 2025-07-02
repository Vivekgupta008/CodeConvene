import json
import re
import logging
from typing import Dict, Any, Optional
from enum import Enum
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from app.core.config import settings
from langsmith import traceable

logger = logging.getLogger(__name__)

class MessageCategory(str, Enum):
    FAQ = "faq"
    TECHNICAL_SUPPORT = "technical_support"
    COMMUNITY_ENGAGEMENT = "community_engagement"
    DOCUMENTATION = "documentation"
    ONBOARDING = "onboarding"
    BUG_REPORT = "bug_report"
    FEATURE_REQUEST = "feature_request"
    WEB_SEARCH = "web_search"
    NOT_CodeConveneEL = "not_CodeConveneel"

class CodeConveneelNeed(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"

class ClassificationRouter:
    """Enhanced message classification with CodeConveneel assessment"""

    def __init__(self, llm_client=None):
        self.llm = llm_client or ChatGoogleGenerativeAI(
            model=settings.classification_agent_model,
            temperature=0.1,
            google_api_key=settings.gemini_api_key
        )
        self._setup_prompts()

    def _setup_prompts(self):
        self.classification_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a CodeConveneel assistant classifier. Analyze messages to determine:
            1. Category (FAQ, Technical Support, Community Engagement, Documentation, Onboarding, Bug Report, Feature Request, Web Search, Not CodeConveneel)
            2. CodeConveneel need level (High, Medium, Low, None)
            3. Suggested agent (CodeConveneel, github, none)
            4. Priority level (high, medium, low)
            
            CodeConveneel Intervention Guidelines:
            - Technical questions about the project: HIGH
            - Onboarding and getting started help: HIGH  
            - Community discussions and engagement: MEDIUM
            - Documentation requests: MEDIUM
            - Bug reports and feature requests: MEDIUM
            - Developer experience feedback: HIGH
            - Web search requests (asking to search for something): HIGH -> WEB_SEARCH
            - Off-topic conversations: NONE
            
            Web Search Indicators:
            - "search for", "look up", "find information about"
            - "what's the latest", "recent news about"
            - "research", "investigate"
            
            Respond ONLY with valid JSON:
            {{
                "category": "category_name",
                "needs_CodeConveneel": true/false,
                "CodeConveneel_need_level": "high|medium|low|none",
                "suggested_agent": "CodeConveneel|github|none",
                "priority": "high|medium|low",
                "confidence": 0.9,
                "reasoning": "brief explanation"
            }}"""),
            ("human", "Message: {message}\nContext: {context}")
        ])

    @traceable(name="user_intent_classification", run_type="llm")
    async def classify_message(self, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Classify a message and determine if CodeConveneel intervention is needed"""
        try:
            # Quick pattern matching for obvious cases
            quick_result = self._quick_classify(message)
            if quick_result:
                return quick_result

            # LLM-based classification for complex cases
            context_str = str(context) if context else "No additional context"

            response = await self.llm.ainvoke(
                self.classification_prompt.format_messages(
                    message=message,
                    context=context_str
                )
            )

            # Parse LLM response
            return self._parse_llm_response(response.content, message)

        except Exception as e:
            logger.error(f"Classification error: {str(e)}")
            return self._fallback_classification(message)

    def _quick_classify(self, message: str) -> Optional[Dict[str, Any]]:
        """Quick pattern-based classification for obvious cases"""
        message_lower = message.lower()

        # Web search patterns
        search_patterns = [
            r"search for", r"look up", r"find information about",
            r"what's the latest", r"recent news about", r"research",
            r"investigate", r"google", r"find out about"
        ]

        if any(re.search(pattern, message_lower) for pattern in search_patterns):
            return {
                "category": MessageCategory.WEB_SEARCH,
                "needs_CodeConveneel": True,
                "CodeConveneel_need_level": CodeConveneelNeed.HIGH,
                "suggested_agent": "CodeConveneel",
                "priority": "high",
                "confidence": 0.9,
                "reasoning": "Web search request pattern match"
            }

        # FAQ patterns
        faq_patterns = [
            r"what is CodeConvene\.?ai",
            r"how do i contribute",
            r"how to get started",
            r"what platforms.*support"
        ]

        for pattern in faq_patterns:
            if re.search(pattern, message_lower):
                return {
                    "category": MessageCategory.FAQ,
                    "needs_CodeConveneel": True,
                    "CodeConveneel_need_level": CodeConveneelNeed.MEDIUM,
                    "suggested_agent": "CodeConveneel",
                    "priority": "medium",
                    "confidence": 0.9,
                    "reasoning": "FAQ pattern match"
                }

        # Bug report patterns
        bug_patterns = [
            r"bug", r"error", r"broken", r"not working", r"issue with"
        ]

        if any(re.search(pattern, message_lower) for pattern in bug_patterns):
            return {
                "category": MessageCategory.BUG_REPORT,
                "needs_CodeConveneel": True,
                "CodeConveneel_need_level": CodeConveneelNeed.HIGH,
                "suggested_agent": "github",
                "priority": "high",
                "confidence": 0.8,
                "reasoning": "Bug report pattern match"
            }

        return None

    def _parse_llm_response(self, response: str, original_message: str) -> Dict[str, Any]:
        """Parse LLM response"""
        try:
            # Extract JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1

            if json_start != -1 and json_end != -1:
                json_str = response[json_start:json_end]
                parsed = json.loads(json_str)
                if "category" in parsed:
                    category_str = parsed["category"].lower()
                    try:
                        category_mapping = {
                            "faq": MessageCategory.FAQ,
                            "web_search": MessageCategory.WEB_SEARCH,
                            "onboarding": MessageCategory.ONBOARDING,
                            "technical_support": MessageCategory.TECHNICAL_SUPPORT,
                            "community_engagement": MessageCategory.COMMUNITY_ENGAGEMENT,
                            "documentation": MessageCategory.DOCUMENTATION,
                            "bug_report": MessageCategory.BUG_REPORT,
                            "feature_request": MessageCategory.FEATURE_REQUEST,
                            "not_CodeConveneel": MessageCategory.NOT_CodeConveneEL
                        }
                        parsed["category"] = category_mapping.get(category_str, MessageCategory.TECHNICAL_SUPPORT)
                    except (KeyError, AttributeError):
                        parsed["category"] = MessageCategory.TECHNICAL_SUPPORT
                return parsed

            raise ValueError("No JSON found in response")

        except Exception as e:
            logger.error(f"Error parsing LLM response: {str(e)}")
            return self._fallback_classification(original_message)

    def _fallback_classification(self, original_message: str) -> Dict[str, Any]:
        """Fallback classification when other methods fail"""
        return {
            "category": MessageCategory.TECHNICAL_SUPPORT,
            "needs_CodeConveneel": True,
            "CodeConveneel_need_level": CodeConveneelNeed.LOW,
            "suggested_agent": "CodeConveneel",
            "priority": "low",
            "confidence": 0.5,
            "reasoning": f"Fallback classification for message: {original_message[:50]}..."
        }
