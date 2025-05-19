from flask import Flask, render_template, redirect, url_for, request, flash, session 
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import abort
import os
import mysql.connector
from app.entity.user_account import UserAccount
from app.entity.user_profile import UserProfile
from app.entity.shortlist import Shortlist
from datetime import datetime
from app import db
from app.entity.service_category import ServiceCategory

from extensions import db

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = 'your_secret_key_here'
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30-minute session timeout
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/C2C_freelance_home_cleaners_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

# Rest of your imports should come after app creation
from app.boundary.public.create_user_page import UserCreatePage
from app.boundary.user_admin.view_user_page import ViewUserPage
from app.boundary.user_admin.update_user_page import UpdateUserPage
from app.boundary.user_admin.suspend_user_page import SuspendUserPage
from app.boundary.user_admin.search_user_page import SearchUserPage
from app.boundary.public.login_page import LoginPage
from app.entity.user_account import UserAccount
from app.entity.cleaning_services import CleaningService

from app.entity.shortlist import Shortlist

from app.controller.homeowner.homeowner_shortlist_controller import HomeownerShortlistController

from app.boundary.platform_management.platform_create_service_category import PlatformCreateServiceCategory

from app.boundary.platform_management.platform_view_service_category import PlatformViewServiceCategory
from app.boundary.platform_management.platform_update_service_category import PlatformUpdateServiceCategory
from app.boundary.platform_management.platform_delete_service_category import PlatformDeleteServiceCategory
from app.boundary.platform_management.platform_search_service_category import PlatformSearchServiceCategory

#from app.boundary.homeowner.homeowner_search_service import homeowner_search_service_bp
from app.boundary.homeowner.homeowner_view_service import HomeownerViewService
from app.boundary.homeowner.homeowner_shortlist import homeowner_shortlist_bp
from app.boundary.homeowner.homeowner_search_shortlist_service import HomeownerSearchShortlistService
from app.boundary.homeowner.homeowner_view_shortlist_service import HomeownerViewShortlistService

from app.boundary.cleaner.cleaner_create_services import service_bp as create_service_bp
#from app.boundary.cleaner.cleaner_search_services import cleaner_bp as search_service_bp
from app.boundary.cleaner.cleaner_view_services import cleaner_bp as view_service_bp
from app.boundary.cleaner.cleaner_update_services import update_bp as update_service_bp
from app.boundary.cleaner.cleaner_delete_services import delete_service_bp
app.register_blueprint(delete_service_bp)
# Cleaner routes
from app.boundary.cleaner.cleaner_search_services import search_bp as cleaner_search_bp
app.register_blueprint(cleaner_search_bp)
# Homeowner routes
from app.boundary.homeowner.homeowner_search_service import homeowner_bp as homeowner_search_bp
app.register_blueprint(homeowner_search_bp)


# Register blueprints
#app.register_blueprint(homeowner_search_bp)
app.register_blueprint(homeowner_shortlist_bp)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'C2C_freelance_home_cleaners_db'
}


# Initialize pages
user_create_page = UserCreatePage()
login_page = LoginPage()
view_user_page = ViewUserPage()
update_user_page = UpdateUserPage()
suspend_user_page = SuspendUserPage()
search_user_page = SearchUserPage()

@app.route("/")
def home():
    return render_template("homepage.html")

def user_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_type' not in session or session['user_type'] != 'User Admin':
            flash("You don't have permission to access this page")
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/verify_code', methods=['POST'])
def verify_code():
    access_code = request.form.get('access_code')
    if access_code == "123":
        return redirect(url_for('create_user'))
    else:
        flash('Invalid access code. Please try again.', 'code_error')
        return redirect(url_for('home'))

# User Management Routes
@app.route('/create_user', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        return user_create_page.create_user_click()
    return user_create_page.display_create_user_form()

# @app.route('/view_users')
# @user_admin_required
# def view_users():
#     from app.entity.user_account import UserAccount

#     users = UserAccount.query.options(db.joinedload(UserAccount.profile)).all()

#     return render_template("admin_view_users.html", users=users)

@app.route('/manage_users')
@user_admin_required
def manage_users():
    users = UserAccount.get_all_users()
    return render_template("admin_manage_users.html", users=users)

# @app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
# @user_admin_required
# def update_user(user_id):
#     user = UserAccount.query.get(user_id)  # Changed from your list-based approach to database query
#     if not user:
#         flash("User not found")
#         return redirect(url_for('manage_users'))
    
#     if request.method == 'POST':
#         new_fullname = request.form.get('fullname')
#         new_phone = request.form.get('phone')
        
#         # Check if phone is already taken by another user
#         existing_user = UserAccount.query.filter(
#             UserAccount.phone == new_phone,
#             UserAccount.id != user_id
#         ).first()
        
#         if existing_user:
#             return render_template("admin_update_users.html", 
#                                user=user, 
#                                phone_error="Phone number already registered by another user")
        
#         try:
#             user.fullname = new_fullname
#             user.phone = new_phone
#             db.session.commit()
#             flash(f"User {user.username} updated successfully!")
#             return redirect(url_for('manage_users'))
#         except Exception as e:
#             db.session.rollback()
#             flash("Error updating user: " + str(e))
#             return render_template("admin_update_users.html", user=user)
    
#     return render_template("admin_update_users.html", user=user)

# @app.route('/suspend_user/<user_id>')
# @user_admin_required
# def suspend_user(user_id):
#     if UserAccount.suspend_user(user_id):   
#         flash("User suspended successfully")
#     else:
#         flash("User not found")
#     return redirect(url_for('manage_users'))

# @app.route('/unsuspend_user/<user_id>')
# @user_admin_required
# def unsuspend_user(user_id):
#     if UserAccount.unsuspend_user(user_id):
#         flash("User unsuspended successfully")
#     else:
#         flash("User not found")
#     return redirect(url_for('manage_users'))

# Update routes
@app.route('/view_users')
@user_admin_required
def view_users():
    return view_user_page.display_all_users()

@app.route('/view_user/<int:user_id>')
@user_admin_required
def view_user(user_id):
    return view_user_page.display_user(user_id)

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
@user_admin_required
def update_user(user_id):
    if request.method == 'POST':
        return update_user_page.update_user(user_id)
    return update_user_page.display_update_form(user_id)



# @app.route('/search_users', methods=['GET', 'POST'])
# @user_admin_required
# def search_users():
#     if request.method == 'POST':
#         return search_user_page.display_search_results()
#     return search_user_page.display_search_form()


@app.route('/suspend_user/<int:user_id>')
@user_admin_required
def suspend_user(user_id):
    return suspend_user_page.suspend_user(user_id)

@app.route('/unsuspend_user/<user_id>')
@user_admin_required
def unsuspend_user(user_id):
    if UserAccount.unsuspend_user(user_id):
        flash("User unsuspended successfully", "success")
    else:
        flash("User not found", "error")
    return redirect(url_for('manage_users'))



# Dashboard Routes
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' not in session:
        flash("Please login first")
        return redirect(url_for('login'))
    if session.get('user_type') != 'User Admin':
        flash("Access denied")
        return redirect(url_for('home'))
    return render_template("user_admin_dashboard.html")

@app.route('/cleaner_dashboard')
def cleaner_dashboard():
    if 'user_id' not in session or session.get('user_type') != 'Cleaner':
        flash('Please login as a cleaner', 'error')
        return redirect(url_for('login'))
    
    services = CleaningService.query.filter_by(cleaner_id=session['user_id']).all()
    print("Found services for dashboard:", services) 
    return render_template("cleaner_dashboard.html", services=services)

@app.route('/homeowner_dashboard')
def homeowner_dashboard():
    if 'username' not in session or session.get('user_type') != 'HomeOwner':
        flash("Access denied")
        return redirect(url_for('home'))
    
    return render_template("homeowner_dashboard.html")



@app.route('/platform_dashboard')
def platform_dashboard():
    if 'username' not in session or session.get('user_type') != 'Platform Management':
        flash("Access denied")
        return redirect(url_for('home'))
    return render_template("platform_dashboard.html")

@app.route('/search_users', methods=['GET', 'POST'])
@user_admin_required
def search_users():
    if request.method == 'POST':
        users = []
        search_term = request.form.get('search_term', '').strip()
        user_profile = request.form.get('user_profile', '').strip()
        query = UserAccount.query.join(UserProfile)
        
        if search_term:
            query = query.filter(
                db.or_(
                    UserAccount.username.contains(search_term),
                    UserAccount.fullname.contains(search_term),
                    UserAccount.phone.contains(search_term)
                )
            )
        
        if user_profile:
            query = query.filter(UserProfile.user_type == user_profile)
        
        users = query.all()
        return render_template("admin_search_users.html", 
                            users=users,
                            search_term=search_term,
                            user_profile=user_profile)
    else:
        return search_user_page.display_search_form()
        
# # Search Functionality
# @app.route('/search_users', methods=['GET', 'POST'])
# @user_admin_required
# def search_users():
#     users = []
#     search_term = ''
#     user_profile = ''

#     if request.method == 'POST':
#         search_term = request.form.get('search_term', '').strip()
#         user_profile = request.form.get('user_profile', '').strip()

#         query = UserAccount.query.join(UserProfile)

#         # Apply text search filter
#         if search_term:
#             query = query.filter(
#                 db.or_(
#                     UserAccount.username.contains(search_term),
#                     UserAccount.fullname.contains(search_term),
#                     UserAccount.phone.contains(search_term)
#                 )
#             )

#         # Apply user profile filter
#         if user_profile:
#             query = query.filter(UserProfile.user_type == user_profile)

#         users = query.all()

#     return render_template("admin_search_users.html", users=users, search_term=search_term, user_profile=user_profile)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return login_page.login_user()
    return login_page.display_login_form()

@app.route('/logout')
def logout():
    return login_page.logout_user()

@app.route('/create-service', methods=['GET', 'POST'])
def create_service():
    if 'user_id' not in session or session.get('user_type') != 'Cleaner':
        flash('Please login as a cleaner', 'warning')
        return redirect(url_for('login'))
    
    # Options for the form
    week_days = [
        {'value': 'monday', 'label': 'Monday'},
        {'value': 'tuesday', 'label': 'Tuesday'},
        {'value': 'wednesday', 'label': 'Wednesday'},
        {'value': 'thursday', 'label': 'Thursday'},
        {'value': 'friday', 'label': 'Friday'},
        {'value': 'saturday', 'label': 'Saturday'},
        {'value': 'sunday', 'label': 'Sunday'}
    ]

    time_slots = [
        {'value': 'morning', 'label': 'Morning (8am - 12pm)'},
        {'value': 'afternoon', 'label': 'Afternoon (12pm - 5pm)'},
        {'value': 'evening', 'label': 'Evening (5pm - 9pm)'}
    ]

    service_categories = [cat[0] for cat in db.session.query(ServiceCategory.category_name).all()]    
    print("Categories going to template:", service_categories)
    if request.method == 'POST':
        
        conn = None
        cursor = None
        
        
        
        
        try:
            current_cleaner_id = session['user_id']
            
            # Debug output
            print(f"Creating service for cleaner ID: {current_cleaner_id}")
            
            # Get form data
            title = request.form['title']
            description = request.form['description']
            location = request.form['location']
            postal_code = request.form['postal_code']
            rate = float(request.form['rate'])
            rate_type = request.form['rate_type']
            min_hours = int(request.form.get('min_hours', 0))
            available_day = request.form['available_day']
            time_slot = request.form['time_slot']
            type_of_cleaning = request.form['type_of_cleaning']
            bring_supplies = request.form['bring_supplies']
            languages = request.form.get('languages', '')

            # Connect to MySQL
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insert data into database
            query = """
            INSERT INTO cleaning_services 
            (cleaner_id, title, description, location, postal_code, rate, rate_type, min_hours, 
             available_day, time_slot, type_of_cleaning, bring_supplies, languages)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (current_cleaner_id, title, description, location, postal_code, 
                     rate, rate_type, min_hours, available_day, time_slot, 
                     type_of_cleaning, bring_supplies, languages)
            
            cursor.execute(query, values)
            conn.commit()

            flash('Service created successfully!', 'success')
            return redirect(url_for('cleaner_dashboard'))

        except mysql.connector.Error as err:
            if conn:
                conn.rollback()
            flash(f'Database error: {err}', 'error')
            return redirect(url_for('create_service'))
        except Exception as e:
            if conn:
                conn.rollback()
            flash(f'Error creating service: {str(e)}', 'error')
            return redirect(url_for('create_service'))
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    return render_template('cleaner_create_service.html',
                         week_days=week_days,
                         time_slots=time_slots,
                         service_categories=service_categories )
    

@app.route('/fix_cleaner_assignments')
def fix_cleaner_assignments():
    if 'user_id' not in session:
        return "Please login first"
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # First nullify all assignments
        cursor.execute("UPDATE cleaning_services SET cleaner_id = NULL")
        
        # Get all services and their creators (assuming you have creation logs)
        cursor.execute("""
            SELECT cs.id, cs.created_by 
            FROM cleaning_services cs
            JOIN users u ON cs.created_by = u.id
            WHERE u.user_type = 'Cleaner'
        """)
        
        services = cursor.fetchall()
        
        # Reassign properly
        for service_id, creator_id in services:
            cursor.execute(
                "UPDATE cleaning_services SET cleaner_id = %s WHERE id = %s",
                (creator_id, service_id)
            )
        
        conn.commit()
        return "Cleaner assignments fixed successfully"
    
    except Exception as e:
        conn.rollback()
        return f"Error: {str(e)}"
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/test_db')
def test_db():
    try:
        # Try to fetch one service
        service = CleaningService.query.first()
        return f"Database connection working. First service title: {service.title if service else 'No services found'}"
    except Exception as e:
        return f"Database error: {str(e)}"
    

@app.route('/view_services')
def view_services():
    if 'user_id' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    
    # Make user_type check case-insensitive
    if session.get('user_type', '').lower() != 'cleaner':
        flash('Only cleaners can view services', 'warning')
        return redirect(url_for('cleaner_dashboard'))
    
    try:
        current_user_id = session['user_id']
        print(f"Attempting to fetch services for cleaner ID: {current_user_id}")
        
        # Using SQLAlchemy to query
        services = CleaningService.query.filter_by(cleaner_id=current_user_id).all()
        print(f"Found {len(services)} services")
        
        return render_template("cleaner_view_services.html", 
                            services=services,
                            current_user_id=current_user_id)
    
    except Exception as e:
        print(f"Error in view_services: {str(e)}")
        flash('Error retrieving services', 'error')
        return redirect(url_for('cleaner_dashboard'))


@app.template_filter('format_rate_type')
def format_rate_type(value):
    rate_types = {
        'hour': 'Per Hour',
        'session': 'Per Session',
        'job': 'Per Job'
    }
    return rate_types.get(value, value.title())

@app.template_filter('format_time_slot')
def format_time_slot(value):
    time_slots = {
        'morning': 'Morning (8AM-12PM)',
        'afternoon': 'Afternoon (12PM-5PM)',
        'evening': 'Evening (5PM-9PM)'
    }
    return time_slots.get(value, value.title())



@app.route('/edit_services')
def edit_services():
    if 'user_id' not in session or session.get('user_type') != 'Cleaner':
        flash('Please login as a cleaner', 'error')
        return redirect(url_for('login'))
    
    services = CleaningService.query.filter_by(cleaner_id=session['user_id']).all()
    return render_template("cleaner_manage_services.html", services=services)


@app.route('/cleaner/service/<int:service_id>/update', methods=['GET', 'POST'])
def update_service(service_id):
    if 'user_id' not in session or session.get('user_type') != 'Cleaner':
        flash('Please login as a cleaner to update services', 'error')
        return redirect(url_for('login'))

    service = CleaningService.query.filter_by(
        id=service_id,
        cleaner_id=session['user_id']
    ).first()

    if not service:
        abort(404)

    if request.method == 'POST':
        try:
            # Validate required fields
            required_fields = ['title', 'description', 'location', 'postal_code', 
                              'rate', 'rate_type', 'available_day', 'time_slot',
                              'type_of_cleaning', 'bring_supplies']
            
            for field in required_fields:
                if field not in request.form or not request.form[field].strip():
                    raise ValueError(f"Missing required field: {field}")

            # Update all fields from the form
            service.title = request.form['title']
            service.description = request.form['description']
            service.location = request.form['location']
            service.postal_code = request.form['postal_code']
            service.rate = float(request.form['rate'])
            service.rate_type = request.form['rate_type']
            service.min_hours = int(request.form.get('min_hours', 0))
            service.available_day = request.form['available_day']
            service.time_slot = request.form['time_slot']
            service.type_of_cleaning = request.form['type_of_cleaning']
            service.bring_supplies = int(request.form['bring_supplies'])
            service.languages = request.form.get('languages', '')
            
            db.session.commit()
            flash('Service updated successfully!', 'success')
            return redirect(url_for('edit_services'))
        
        except ValueError as e:
            db.session.rollback()
            flash(str(e), 'error')
            return redirect(url_for('update_service', service_id=service.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating service: {str(e)}', 'error')
            return redirect(url_for('update_service', service_id=service.id))
    
    # For GET requests, render the update form
    week_days = [
        {'value': 'monday', 'label': 'Monday'},
        {'value': 'tuesday', 'label': 'Tuesday'},
        {'value': 'wednesday', 'label': 'Wednesday'},
        {'value': 'thursday', 'label': 'Thursday'},
        {'value': 'friday', 'label': 'Friday'},
        {'value': 'saturday', 'label': 'Saturday'},
        {'value': 'sunday', 'label': 'Sunday'}
    ]

    time_slots = [
        {'value': 'morning', 'label': 'Morning (8am - 12pm)'},
        {'value': 'afternoon', 'label': 'Afternoon (12pm - 5pm)'},
        {'value': 'evening', 'label': 'Evening (5pm - 9pm)'}
    ]

    cleaning_types = [
    {'value': c.category_name, 'label': c.category_name}
    for c in db.session.query(ServiceCategory).all()
    ]

    return render_template('cleaner_update_services.html', 
                         service=service,
                         week_days=week_days,
                         time_slots=time_slots,
                         cleaning_types=cleaning_types)

# Temporary route to fix existing data
@app.route('/fix_cleaner_ids')
def fix_cleaner_ids():
    if 'user_id' not in session:
        return "Please login first"
    
    # Update all services to belong to current user
    CleaningService.query.update({'cleaner_id': session['user_id']})
    db.session.commit()
    
    return "Updated all services to belong to current user"

@app.route('/assign_services_to_user')
def assign_services_to_user():
    if 'user_id' not in session:
        return "Please login first"
    
    # Get current user's ID
    user_id = session['user_id']
    
    # Update all services to belong to this user
    CleaningService.query.update({'cleaner_id': user_id})
    db.session.commit()
    
    return f"All services assigned to user {user_id}"



@app.route('/search_services', methods=['GET', 'POST'])
def search_services():
    if 'user_id' not in session or session.get('user_type') != 'Cleaner':
        flash('Please login as a cleaner to search services', 'error')
        return redirect(url_for('login'))
    
    # Get filter options for the dropdowns
    available_days = db.session.query(
        CleaningService.available_day
    ).filter_by(cleaner_id=session['user_id']).distinct().all()
    
    time_slots = db.session.query(
        CleaningService.time_slot
    ).filter_by(cleaner_id=session['user_id']).distinct().all()
    
    cleaning_types = db.session.query(
        CleaningService.type_of_cleaning
    ).filter_by(cleaner_id=session['user_id']).distinct().all()
    
    if request.method == 'POST':
        available_day = request.form.get('available_day')
        time_slot = request.form.get('time_slot')
        type_of_cleaning = request.form.get('type_of_cleaning')
        
        # Build the query
        query = CleaningService.query.filter_by(cleaner_id=session['user_id'])
        
        if available_day:
            query = query.filter(CleaningService.available_day == available_day)
        if time_slot:
            query = query.filter(CleaningService.time_slot == time_slot)
        if type_of_cleaning:
            query = query.filter(CleaningService.type_of_cleaning == type_of_cleaning)
        
        services = query.all()
        
        return render_template('cleaner_search_results.html', 
                            services=services,
                            available_days=[day[0] for day in available_days],
                            time_slots=[slot[0] for slot in time_slots],
                            cleaning_types=[ctype[0] for ctype in cleaning_types])
    
    return render_template('cleaner_search_services.html',
                         available_days=[day[0] for day in available_days],
                         time_slots=[slot[0] for slot in time_slots],
                         cleaning_types=[ctype[0] for ctype in cleaning_types])
    

from app.boundary.cleaner.cleaner_match_history import CleanerMatchHistory
from app.boundary.cleaner.cleaner_view_tracking import CleanerViewTracking


@app.route('/cleaner/view_tracking')
def cleaner_view_tracking():
    return CleanerViewTracking().display()

@app.route('/cleaner/match_history')
def cleaner_match_history():
    return CleanerMatchHistory().display()




##Homeowner Routes
from app.boundary.homeowner.homeowner_match_service import HomeownerMatchService 
@app.route('/homeowner_search_services', methods=['GET', 'POST'])
def homeowner_search_services():
    if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
        flash('Please login as a homeowner to search for services', 'error')
        return redirect(url_for('login'))
    
    # Get filter options across all available services (not limited to a specific user)
    available_days = db.session.query(
        CleaningService.available_day
    ).distinct().all()
    
    time_slots = db.session.query(
        CleaningService.time_slot
    ).distinct().all()
    
    cleaning_types = db.session.query(
        CleaningService.type_of_cleaning
    ).distinct().all()
    
    if request.method == 'POST':
        available_day = request.form.get('available_day')
        time_slot = request.form.get('time_slot')
        type_of_cleaning = request.form.get('type_of_cleaning')
        
        # Build the query for all services (not user-specific)
        query = CleaningService.query
        
        if available_day:
            query = query.filter(CleaningService.available_day == available_day)
        if time_slot:
            query = query.filter(CleaningService.time_slot == time_slot)
        if type_of_cleaning:
            query = query.filter(CleaningService.type_of_cleaning == type_of_cleaning)
        
        services = query.all()
        
        return render_template('homeowner_search_results.html', 
                            services=services,
                            available_days=[day[0] for day in available_days],
                            time_slots=[slot[0] for slot in time_slots],
                            cleaning_types=[ctype[0] for ctype in cleaning_types])
    
    return render_template('homeowner_search_services.html',
                         available_days=[day[0] for day in available_days],
                         time_slots=[slot[0] for slot in time_slots],
                         cleaning_types=[ctype[0] for ctype in cleaning_types])


@app.route('/homeowner/view_service/<int:service_id>', methods=['GET'])
def homeowner_view_service_details(service_id):
    if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
        flash('Please login as a homeowner to view services.', 'error')
        return redirect(url_for('login'))

    # Fetch service and cleaner info
    service = CleaningService.query.get_or_404(service_id)
    ##cleaner = UserProfile.query.get(service.cleaner_id)
    cleaner= UserAccount.query.get(service.cleaner_id)
    from extensions import db
    from app.entity.service_views import ServiceViews


    viewer_id = session.get('user_id')
    if viewer_id and viewer_id != service.cleaner_id:  # don’t count the owner
        db.session.add(ServiceViews(service_id=service.id, viewer_id=viewer_id))
        db.session.commit()

    return render_template('homeowner_view_service.html', service=service, cleaner=cleaner)


@app.route('/homeowner/save_to_shortlist/<int:service_id>', methods=['POST'])
def save_to_shortlist(service_id):
    if 'user_id' not in session or session.get('user_type') != 'HomeOwner':
        flash('Please login as a homeowner to save services.', 'error')
        return redirect(url_for('login'))
    
    if HomeownerShortlistController.add_to_shortlist(session['user_id'], service_id):
        flash('Service saved to your shortlist!', 'success')
    else:
        flash('This service is already in your shortlist.', 'info')
    
    return redirect(url_for('homeowner_view_service_details', service_id=service_id))


@app.route('/homeowner/shortlist/search', methods=['GET'])
def search_shortlist():
    return HomeownerSearchShortlistService.search_shortlist()

@app.route('/homeowner/shortlist', methods=['GET'])
def view_shortlist():
    return HomeownerViewShortlistService.view_shortlist()

@app.route('/homeowner/shortlist/search', methods=['GET', 'POST'])
def homeowner_search_shortlist():
    homeowner_id = session['user_id']  #  Here in app.py
    search_query = request.form.get('search_query') if request.method == 'POST' else None
    shortlisted_services = HomeownerShortlistController.get_shortlisted_services(homeowner_id, search_query)
    
    return render_template('homeowner_shortlist.html', services=shortlisted_services)

@app.route('/homeowner/match_service')
def homeowner_match_service():
    return HomeownerMatchService().confirm_match()

from app.boundary.homeowner.homeowner_match_history import HomeownerMatchHistory

@app.route('/homeowner/match_history')
def homeowner_match_history():
    return HomeownerMatchHistory().display() 


@app.route('/platform/create_service_category')
def platform_create_category():
    return PlatformCreateServiceCategory().display_form()

@app.route('/platform/submit_service_category', methods=['POST'])
def submit_service_category():
    return PlatformCreateServiceCategory().submit_form()

@app.route('/platform/view_service_category')
def view_service_category():
    return PlatformViewServiceCategory.view_categories()

@app.route('/platform/update_service_category/<int:category_id>', methods=['POST'])
def update_service_category(category_id):
    return PlatformUpdateServiceCategory.update_category(category_id)

@app.route('/platform/delete_service_category/<int:category_id>', methods=['POST'])
def delete_service_category(category_id):
    return PlatformDeleteServiceCategory.delete_category(category_id)

@app.route('/platform/search_service_category', methods=['GET', 'POST'])
def search_service_category():
    return PlatformSearchServiceCategory.search_categories()

from app.boundary.platform_management.platform_user_report import PlatformUserReport

@app.route('/platform/user_report')
def platform_user_report():
   
    return PlatformUserReport().display_report()



from flask import Response
from io import StringIO
import csv
from app.boundary.platform_management.platform_user_report import PlatformUserReport

@app.route('/platform/user_report/download')
def download_user_report():
    group_by = request.args.get('group_by', 'monthly')
    return PlatformUserReport().download_report_csv(group_by)

if __name__ == "__main__":
    app.run(debug=True)