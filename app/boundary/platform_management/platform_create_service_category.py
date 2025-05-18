from flask import render_template, request, redirect, url_for, flash
from app.controller.platform_management.platform_create_service_category_controller import PlatformCreateServiceCategoryController

class PlatformCreateServiceCategory:
    def __init__(self):
        self.controller = PlatformCreateServiceCategoryController()
    
    def display_form(self):
        return render_template('platform_create_category.html')
    
    def submit_form(self):
        category_name = request.form.get('category_name')
        if category_name:
            if self.controller.category_exists(category_name):
                flash(f"Category '{category_name}' already exists!", "error")
                return redirect(url_for('platform_create_category'))
            else:
                self.controller.add_category(category_name)
                flash("Category added successfully!", "success")
        return redirect(url_for('view_service_category'))
    