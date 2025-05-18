from extensions import db
from datetime import datetime

class ServiceViews(db.Model):
    tablename = 'service_views'

    id         = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('cleaning_services.id'), nullable=False)
    viewer_id  = db.Column(db.Integer, db.ForeignKey('user_account.id'),      nullable=False)
    view_time  = db.Column(db.DateTime, default=datetime.utcnow)

    service = db.relationship('CleaningService', backref='views')
    viewer  = db.relationship('UserAccount', foreign_keys=[viewer_id])