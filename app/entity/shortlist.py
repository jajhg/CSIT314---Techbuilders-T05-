from app import db
from app.entity.cleaning_services import CleaningService
from app.entity.user_account import UserAccount
from datetime import datetime

class Shortlist(db.Model):
    tablename = 'shortlist'

    id = db.Column(db.Integer, primary_key=True)
    homeowner_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('cleaning_services.id'), nullable=False)  
    
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)  #  Add this line

    service = db.relationship('CleaningService', backref='shortlisted_by')
    homeowner = db.relationship('UserAccount', backref='shortlisted_services')