from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) #  datarequired validator -> Checks the field's data is 'truthy' otherwise stops the validation chain
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) #  email validator -> Validates an email address 
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]) #  equalTo validator -> check if the value is identical to 'password' field
    submit = SubmitField('Register')

    def validate_username(self, username):
        temp_user = User.query.filter_by(username=username.data).first()
        if temp_user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        temp_email = User.query.filter_by(email=email.data).first()
        if temp_email is not None:
            raise ValidationError('Please use a different email address.')