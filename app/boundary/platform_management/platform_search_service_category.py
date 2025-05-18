from flask import request, render_template
from app.controller.platform_management.platform_search_service_category_controller import PlatformSearchServiceCategoryController

class PlatformSearchServiceCategory:
    @staticmethod
    def search_categories():
        keyword = request.args.get('keyword', '')
        results = PlatformSearchServiceCategoryController.search_categories(keyword)
        return render_template('view_service_category.html', categories=results)