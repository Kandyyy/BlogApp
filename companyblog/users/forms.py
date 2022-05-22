from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords do not match!")])
    pass_confirm = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already under use!")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username has already been registered!")

class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField("Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")
    
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already under use!")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username has already been registered!")
