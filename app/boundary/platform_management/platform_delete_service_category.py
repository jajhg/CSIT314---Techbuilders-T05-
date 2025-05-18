from flask import redirect, url_for, flash
from app.controller.platform_management.platform_delete_service_category_controller import PlatformDeleteServiceCategoryController

class PlatformDeleteServiceCategory:
    @staticmethod
    def delete_category(category_id):
        if PlatformDeleteServiceCategoryController.delete_category(category_id):
            flash("Category deleted successfully.", "success")
        else:
            flash("Category not found", "error")
        return redirect(url_for('view_service_category'))