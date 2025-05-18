from app.entity.service_category import ServiceCategory

class PlatformSearchServiceCategoryController:
    @staticmethod
    def search_categories(keyword):
        return ServiceCategory.query.filter(
            ServiceCategory.category_name.ilike(f'%{keyword}%')
        ).all()