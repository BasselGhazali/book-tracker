from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(user=form.name.data, email=form.email.data, password=form.password.data)
        flash("Registration successful!")
        return redirect(url_for('authentication.log_in_user'))

    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def log_in_user():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid credentials, please try again')
            return redirect(url_for('authentication.log_in_user'))

        login_user(user, form.stay_logged_in.data)
        return redirect(url_for('main.display_books'))

    return render_template('login.html', form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
