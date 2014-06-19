from datetime import datetime
from flask import current_app, render_template, session, redirect, url_for
from . import main
from .forms import RegistrationForm
from .. import db
from ..models import User
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
    print(current_app.config) # Debugging, remove later
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.first = form.first_name.data
        user.last = form.last_name.data
        user.city = form.city.data
        user.dob = form.dob.data
        user.gender = form.gender.data
        user.home_box = form.home_box.data
        user.state = form.state.data
        user.street_addr1 = form.street_addr1.data
        user.street_addr2 = form.street_addr2.data
        user.zip = form.zip.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit

        if current_app.config['ADMIN']:
            send_email(current_app.config['ADMIN'], 'Athlete Registration', 'mail/new_user', user=user)

        return redirect(url_for('.index'))

    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
