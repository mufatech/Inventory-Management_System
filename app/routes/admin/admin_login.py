from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.admin import Admin
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin = request.form.get('admin')
        password = request.form.get('password')

            # Log in the admin user
            login_user(admin)

            flash('You are now the admin. Welcome!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            # Admins exist, so check the entered credentials
            admin = Admin.query.filter_by(admin=admin).first()
            if admin and admin.check_password(password):
                # Log in the admin user
                login_user(admin)
                flash('Login successful!', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid login details.', 'danger')

    return render_template("admin/login.html")




@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('admin_login'))

