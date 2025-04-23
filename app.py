from flask import Flask, render_template, redirect, url_for, request, flash

# Specify the templates folder inside the 'app' directory
app = Flask(__name__, template_folder='app/templates')
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Home Page (User Management)
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("user_management.html")

# Route for creating user
@app.route('/create_user', methods=["GET", "POST"])
def show_create_user_form():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")

        # Print or save user data here (simulating user creation)
        print(f"Username: {username}, Email: {email}")

        # Flash success message
        flash(f"User '{username}' created successfully with email {email}!", 'success')

        # Redirect to home page (or wherever you'd like to redirect after form submission)
        return redirect(url_for('home'))  # Redirect to home after submitting the form

    return render_template("user_create.html")

if __name__ == "__main__":
    app.run(debug=True)
