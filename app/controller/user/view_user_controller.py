from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from extensions import db

class ViewUserController:
    @staticmethod
    def get_all_users():
        """Get all users with their profiles"""
        return UserAccount.query.options(db.joinedload(UserAccount.profile)).all()

    @staticmethod
    def get_user_by_id(user_id):
        """Get a single user by ID with profile"""
        return UserAccount.query.options(db.joinedload(UserAccount.profile)).get(user_id)