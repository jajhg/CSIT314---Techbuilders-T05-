from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from extensions import db

class SuspendUserController:
    @staticmethod
    def suspend_user(user_id):
        user = UserAccount.query.get(user_id)
        if not user:
            return False
            
        try:
            user.is_suspended = True
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def unsuspend_user(user_id):
        user = UserAccount.query.get(user_id)
        if not user:
            return False
            
        try:
            user.is_suspended = False
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False