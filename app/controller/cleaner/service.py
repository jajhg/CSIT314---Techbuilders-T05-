from datetime import time
from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from app.entity.enums import CleaningType, SupplyOption, TimeSlot
from extensions import db

class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    cleaner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    rate_type = db.Column(db.String(20), nullable=False)  # 'hour', 'session', 'job'
    min_hours = db.Column(db.Integer)
    days_available = db.Column(db.String(100), nullable=False)  # Comma-separated days
    time_slots = db.Column(db.String(100), nullable=False)  # Comma-separated time slots
    cleaning_types = db.Column(db.String(200), nullable=False)  # Comma-separated types
    supplies = db.Column(db.Enum(SupplyOption), nullable=False)
    languages = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), 
                         onupdate=db.func.current_timestamp())

    def __init__(self, cleaner_id, title, description, location, postal_code, 
                 rate, rate_type, min_hours, days_available, time_slots, 
                 cleaning_types, supplies, languages=None):
        self.cleaner_id = cleaner_id
        self.title = title
        self.description = description
        self.location = location
        self.postal_code = postal_code
        self.rate = rate
        self.rate_type = rate_type
        self.min_hours = min_hours
        self.days_available = days_available
        self.time_slots = time_slots
        self.cleaning_types = cleaning_types
        self.supplies = supplies
        self.languages = languages