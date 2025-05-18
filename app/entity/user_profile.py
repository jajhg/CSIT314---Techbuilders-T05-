from extensions import db
from app.entity.user_account import UserAccount

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    
    id = db.Column(db.Integer, db.ForeignKey('user_account.id'), primary_key=True)
    user_type = db.Column(db.Enum('User Admin', 'Cleaner', 'HomeOwner', 'Platform Management'), nullable=False)
    
    # Relationship back to UserAccount
    user = db.relationship("UserAccount", back_populates="profile")