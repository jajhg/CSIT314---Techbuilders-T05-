# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/C2C_freelance_home_cleaners_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False