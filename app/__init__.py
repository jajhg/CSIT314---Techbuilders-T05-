# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/C2C_freelance_home_cleaners_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import models here so they register with the db
    from app.entity.user_account import UserAccount
    from app.entity.user_profile import UserProfile
    from app.entity.cleaning_services import CleaningService

    
    # Import the cleaner blueprint
    from app.boundary.cleaner.cleaner_search_services import cleaner_bp

    # Register it with the app
    app.register_blueprint(cleaner_bp)

    with app.app_context():
        db.create_all()

    return app