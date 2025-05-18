from extensions import db
from datetime import datetime

class ServiceMatches(db.Model):
    tablename = 'service_matches'

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('cleaning_services.id'))
    homeowner_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    cleaner_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    match_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ServiceMatch {self.id}>'
    # Optional relationships (can be used if needed)
    service = db.relationship('CleaningService', backref='matches')
    homeowner = db.relationship('UserAccount', foreign_keys=[homeowner_id])
    cleaner = db.relationship('UserAccount', foreign_keys=[cleaner_id])