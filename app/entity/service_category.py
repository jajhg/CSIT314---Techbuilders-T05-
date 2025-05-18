from app import db

class ServiceCategory(db.Model):
    __tablename__ = 'service_category'
    
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<ServiceCategory {self.category_name}>'