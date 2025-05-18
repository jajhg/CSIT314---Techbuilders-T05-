from app.entity.service_category import ServiceCategory
from app import db
from sqlalchemy.exc import IntegrityError

class PlatformUpdateServiceCategoryController:
    @staticmethod
    def update_category(category_id, new_name):
        # First check if another category with this name already exists
        existing_category = ServiceCategory.query.filter(
            ServiceCategory.category_name == new_name,
            ServiceCategory.category_id != category_id
        ).first()
        
        if existing_category:
            return False  # Indicate duplicate name exists
        
        category = ServiceCategory.query.get(category_id)
        if category:
            try:
                category.category_name = new_name
                db.session.commit()
                return True
            except IntegrityError:
                db.session.rollback()
                return False
        return False