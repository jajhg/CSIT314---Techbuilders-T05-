from flask import redirect, url_for, request, flash
from app.controller.platform_management.platform_update_service_category_controller import PlatformUpdateServiceCategoryController

class PlatformUpdateServiceCategory:
    @staticmethod
    def update_category(category_id):
        new_name = request.form.get('new_name')
        if new_name:
            result = PlatformUpdateServiceCategoryController.update_category(category_id, new_name)
            if result is None:
                flash("Category not found", "error")
            elif result is False:
                flash("There is already a service category with the same name, please try another name.", "error")
            else:
                flash("Category updated successfully!", "success")
        return redirect(url_for('view_service_category'))