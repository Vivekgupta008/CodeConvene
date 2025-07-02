import logging
import json
from typing import Optional, Dict, Any
from datetime import datetime, timezone
from app.models.database.weaviate import WeaviateUserProfile
from app.database.weaviate.client import get_weaviate_client
import weaviate.exceptions as weaviate_exceptions
import weaviate.classes as wvc

logger = logging.getLogger(__name__)

class WeaviateUserOperations:
    """
    Class to handle Weaviate operations for user profiles.
    """

    def __init__(self, collection_name: str = "weaviate_user_profile"):
        self.collection_name = collection_name

    async def find_user_by_id(self, user_id: str) -> Optional[str]:
        """
        Find a user profile by user_id and return the UUID if found.
        """
        try:
            async with get_weaviate_client() as client:
                collection = client.collections.get(self.collection_name)

                response = await collection.query.fetch_objects(
                    where=wvc.query.Filter.by_property("user_id").equal(user_id),
                    limit=1
                )

                if response.objects:
                    found_uuid = str(response.objects[0].uuid)
                    logger.info(f"Found existing user profile with UUID: {found_uuid}")
                    return found_uuid
                return None

        except weaviate_exceptions.WeaviateBaseError as e:
            logger.error(f"Weaviate error finding user by ID: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error finding user by ID: {str(e)}")
            return None

    async def create_user_profile(self, profile: WeaviateUserProfile) -> bool:
        """
        Create a new user profile in Weaviate.
        """
        try:
            profile_dict = self._prepare_profile_data(profile)

            async with get_weaviate_client() as client:
                collection = client.collections.get(self.collection_name)

                result = await collection.data.insert(
                    properties=profile_dict
                )

            logger.info(f"Created user profile for {profile.github_username} with UUID: {result}")
            return True

        except weaviate_exceptions.WeaviateBaseError as e:
            logger.error(f"Weaviate error creating user profile: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error creating user profile: {str(e)}")
            return False

    async def update_user_profile(self, uuid: str, profile: WeaviateUserProfile) -> bool:
        """
        Update an existing user profile in Weaviate.
        """
        try:
            profile_dict = self._prepare_profile_data(profile)

            async with get_weaviate_client() as client:
                collection = client.collections.get(self.collection_name)
                await collection.data.update(
                    uuid=uuid,
                    properties=profile_dict
                )

            logger.info(f"Updated user profile for {profile.github_username} with UUID: {uuid}")
            return True

        except weaviate_exceptions.WeaviateBaseError as e:
            logger.error(f"Weaviate error updating user profile: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error updating user profile: {str(e)}")
            return False

    async def upsert_user_profile(self, profile: WeaviateUserProfile) -> bool:
        """
        Create or update a user profile (upsert operation).
        """
        try:
            existing_uuid = await self.find_user_by_id(profile.user_id)

            if existing_uuid:
                logger.info(f"Updating existing profile for user_id: {profile.user_id}")
                return await self.update_user_profile(existing_uuid, profile)
            else:
                logger.info(f"Creating new profile for user_id: {profile.user_id}")
                return await self.create_user_profile(profile)

        except Exception as e:
            logger.error(f"Error in upsert operation: {str(e)}")
            return False

    def _prepare_profile_data(self, profile: WeaviateUserProfile) -> Dict[str, Any]:
        """
        Prepare profile data for Weaviate storage.
        """
        profile_dict = profile.model_dump()

        profile_dict["repositories"] = json.dumps([repo.model_dump() for repo in profile.repositories])
        profile_dict["pull_requests"] = json.dumps([pr.model_dump() for pr in profile.pull_requests])

        if isinstance(profile.last_updated, datetime):
            if profile.last_updated.tzinfo is None:
                profile.last_updated = profile.last_updated.replace(tzinfo=timezone.utc)
            profile_dict["last_updated"] = profile.last_updated.isoformat()
        else:
            profile_dict["last_updated"] = datetime.now(timezone.utc).isoformat()

        return profile_dict


async def store_user_profile(profile: WeaviateUserProfile) -> bool:
    """
    Convenience function to store or update a user profile.
    """
    operations = WeaviateUserOperations()
    return await operations.upsert_user_profile(profile)
