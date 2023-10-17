from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256

from .models.User import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def get_authenticated_user(self) -> User:
        user = User.query.get(self.email.data)
        if user is None:
            return None
        # m = sha256()
        # m.update(self.password.data.encode())
        # passwd = m.hexdigest()
        passwd = self.password.data
        return user if passwd == user.get_password() else None