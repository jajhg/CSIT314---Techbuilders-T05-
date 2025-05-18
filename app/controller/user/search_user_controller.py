from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from sqlalchemy import or_

class SearchUserController:
    @staticmethod
    def search_users(search_term=None, user_profile=None):
        """Search users with optional filters"""
        query = UserAccount.query.join(UserProfile)
        
        # Apply text search filter
        if search_term:
            query = query.filter(
                or_(
                    UserAccount.username.contains(search_term),
                    UserAccount.fullname.contains(search_term),
                    UserAccount.phone.contains(search_term)
                )
            )
        
        # Apply user profile filter
        if user_profile:
            query = query.filter(UserProfile.user_type == user_profile)
            
        return query.all()