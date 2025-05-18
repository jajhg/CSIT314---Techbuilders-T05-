from datetime import datetime
from extensions import db

class CleaningService(db.Model):
    __tablename__ = 'cleaning_services'

    id = db.Column(db.Integer, primary_key=True)
    cleaner_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    rate_type = db.Column(db.String(20), nullable=False)
    min_hours = db.Column(db.Integer)
    available_day = db.Column(db.String(20), nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)
    type_of_cleaning = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('service_category.category_id'))
    category = db.relationship('ServiceCategory')
    bring_supplies = db.Column(db.String(10), nullable=False)
    languages = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<CleaningService {self.title}>'