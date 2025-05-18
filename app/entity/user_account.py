from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class UserAccount(db.Model):
    __tablename__ = 'user_account'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(100))
    phone = db.Column(db.String(20), unique=True)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.Enum('Male', 'Female', 'Other'))
    is_suspended = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                         onupdate=db.func.current_timestamp())

    # Relationship to UserProfile
    profile = db.relationship("UserProfile", back_populates="user", uselist=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()

    @classmethod
    def authenticate(cls, username, password):
        user = cls.find_by_username(username)
        if user and user.verify_password(password):
            if user.is_suspended:
                raise ValueError("Your account has been suspended. Please contact the user admins.")
            return user
        return None
    
    @classmethod
    def get_all_users(cls):
        """Get all users"""
        return cls.query.all()

    @classmethod
    def suspend_user(cls, user_id):
        """Suspend a user account"""
        user = cls.query.get(user_id)
        if user:
            user.is_suspended = True
            db.session.commit()
            return True
        return False

    @classmethod
    def unsuspend_user(cls, user_id):
        """Unsuspend a user account"""
        user = cls.query.get(user_id)
        if user:
            user.is_suspended = False
            db.session.commit()
            return True
        return False
from app.entity.user_profile import UserProfile

UserAccount.profile = db.relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")