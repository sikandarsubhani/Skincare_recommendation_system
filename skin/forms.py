from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length, Regexp
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from skin.models import User

class RegisterForm(FlaskForm):
  
  def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
  def validate_email_address(self, email_address_to_check):
        email= User.query.filter_by(email=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')


  username=StringField(label='User Name',validators=[Length(min=2,max=30,message="Username must be atleast 5 character"),DataRequired()])
  email=StringField(label='E-mail',validators=[Email(),DataRequired()])
  password1=PasswordField(label='Password',validators=[Length(min=6),DataRequired()])
  password2=PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
  submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')