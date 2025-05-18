from app.entity.service_category import ServiceCategory
from app import db

class PlatformViewServiceCategoryController:
    @staticmethod
    def get_all_categories():
        return ServiceCategory.query.all()
    
    @staticmethod
    def search_categories(keyword):
        return ServiceCategory.query.filter(
            ServiceCategory.category_name.ilike(f'%{keyword}%')
        ).all()