from app.entity.service_category import ServiceCategory
from app import db

class PlatformDeleteServiceCategoryController:
    @staticmethod
    def delete_category(category_id):
        category = ServiceCategory.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False