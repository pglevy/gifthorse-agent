from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms import UpdateProfileForm
from app import db

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def view_profile():
    return render_template('profile.html', user=current_user)

@profile.route('/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('profile.view_profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
    return render_template('profile.html', form=form)
