from flask.ext.wtf import Form
from wtforms import DateField, SelectField, StringField, SubmitField
from wtforms.validators import Required

class RegistrationForm(Form):
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
    username = StringField('Username', validators = [Required()])
    password = StringField('Password', validators = [Required()])
    submit = SubmitField('Submit')

