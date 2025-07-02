from enum import Enum

class PlatformType(str, Enum):
    GITHUB = "github"
    DISCORD = "discord"
    SLACK = "slack"
    DISCOURSE = "discourse"
    SYSTEM = "system"

class EventType(str, Enum):
    ISSUE_CREATED = "issue.created"
    ISSUE_CLOSED = "issue.closed"
    ISSUE_UPDATED = "issue.updated"
    ISSUE_COMMENTED = "issue.commented"
    PR_CREATED = "pr.created"
    PR_UPDATED = "pr.updated"
    PR_COMMENTED = "pr.commented"
    PR_MERGED = "pr.merged"

    PR_REVIEWED = "pr.reviewed"
    
    MESSAGE_CREATED = "message.created"
    MESSAGE_UPDATED = "message.updated"
    MESSAGE_DELETED = "message.deleted"
    REACTION_ADDED = "reaction.added"
    USER_JOINED = "user.joined"
    
    ONBOARDING_STARTED = "onboarding.started"
    ONBOARDING_COMPLETED = "onboarding.completed"
    FAQ_REQUESTED = "faq.requested"
    KNOWLEDGE_UPDATED = "knowledge.updated"
    ANALYTICS_COLLECTED = "analytics.collected"

