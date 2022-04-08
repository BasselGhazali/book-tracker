from flask import render_template, request, flash, redirect, url_for
from app.auth.forms import RegistrationForm
from app.auth import authentication as at
from app.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(user=form.name.data, email=form.email.data, password=form.password.data)
        flash("Registration successful!")
        return redirect(url_for('at.login_user'))

    return render_template('registration.html', form=form)
