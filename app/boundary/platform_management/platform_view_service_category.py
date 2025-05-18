from flask import render_template, request
from app.controller.platform_management.platform_view_service_category_controller import PlatformViewServiceCategoryController

class PlatformViewServiceCategory:
    @staticmethod
    def view_categories():
        categories = PlatformViewServiceCategoryController.get_all_categories()
        return render_template('view_service_category.html', categories=categories)
    
    @staticmethod
    def search_categories():
        keyword = request.args.get('keyword', '')
        results = PlatformViewServiceCategoryController.search_categories(keyword)
        return render_template('view_service_category.html', categories=results)