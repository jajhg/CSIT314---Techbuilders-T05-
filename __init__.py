# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import models
    from app.entity import user_account, cleaning_service

    # Register blueprints
    from app.boundary.public.routes import public_bp
    from app.boundary.admin.routes import admin_bp
    from app.boundary.cleaner.routes import cleaner_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(cleaner_bp)

    return app