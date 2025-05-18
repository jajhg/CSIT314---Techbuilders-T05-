from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from extensions import db

class UpdateUserController:
    @staticmethod
    def validate_phone(phone, current_user_id=None):
        """Validate phone number and check for duplicates"""
        if len(phone) != 8 or not phone.isdigit():
            raise ValueError("Phone number must be exactly 8 digits")
            
        existing_user = UserAccount.query.filter(
            UserAccount.phone == phone,
            UserAccount.id != current_user_id
        ).first()
        
        if existing_user:
            raise ValueError("Phone number already registered by another user")

    @staticmethod
    def update_user(user_id, fullname, phone, user_type):
        """Update user details and profile"""
        try:
            user = UserAccount.query.get(user_id)
            if not user:
                return False, "User not found"

            # Validate phone using the separate method
            try:
                UpdateUserController.validate_phone(phone, user_id)
            except ValueError as e:
                return False, str(e)

            # Update user account
            user.fullname = fullname
            user.phone = phone
            
            # Update user profile
            if not user.profile:
                # Create profile if it doesn't exist
                user.profile = UserProfile(user_type=user_type)
            else:
                user.profile.user_type = user_type
                
            db.session.commit()
            return True, f"User {user.username} updated successfully!"
        
        except Exception as e:
            db.session.rollback()
            return False, f"Error updating user: {str(e)}"