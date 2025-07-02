CONVERSATION_SUMMARY_PROMPT = """You are a CodeConveneel assistant. Create a concise summary of this conversation.

EXISTING SUMMARY:
{existing_summary}

RECENT CONVERSATION:
{recent_conversation}

USER PROFILE:
{user_profile}

Instructions:
1. Create a NEW summary combining existing and recent conversation
2. Focus on user's technical interests, problems, and experience level
3. Keep under 300 words
4. Include relevant context for future interactions

NEW SUMMARY:"""
