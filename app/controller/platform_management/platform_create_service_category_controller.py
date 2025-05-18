from app.entity.service_category import ServiceCategory
from app import db

class PlatformCreateServiceCategoryController:
    def __init__(self):
        self.db_session = db.session
    
    def add_category(self, category_name):
        new_category = ServiceCategory(category_name=category_name)
        db.session.add(new_category)
        db.session.commit()
    
    def category_exists(self, category_name):
        return self.db_session.query(ServiceCategory).filter_by(
            category_name=category_name
        ).first() is not None
    