from flask.ext.wtf import Form
from wtforms_html5 import DateField
from wtforms import SelectField, StringField, SubmitField, PasswordField
from wtforms.validators import Required, EqualTo
from wtforms import widgets

class RegistrationForm(Form):
    email = StringField('Email', validators = [Required()])
    password = PasswordField('Password', validators = [
        Required(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators = [Required()])
    first_name = StringField('First name', validators = [Required()])
    last_name = StringField('Last name', validators = [Required()])
    dob = DateField()
    street_addr1 = StringField('Street 1')
    street_addr2 = StringField('Street 2')
    city = StringField('City')
    state = StringField('State')
    zip = StringField('Zip')
    gender = SelectField(u'Gender', choices=[('M', 'M'), ('F', 'F')])
    home_box = StringField('Home Box')
    submit = SubmitField('Submit')

