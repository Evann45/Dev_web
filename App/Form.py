from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import DataRequired
from hashlib import sha256

from .models.User import User, UserDB
from .models.Post import Post, PostDB

import datetime


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()

    def get_authenticated_user(self) -> User:
        user = User.query.get(self.email.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        if passwd == user.get_password():
            return user
        return None

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    pseudo = StringField('Pseudo', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def create_account(self) -> None:
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        UserDB.insert_new_user(self.email.data, self.pseudo.data, self.nom.data, self.prenom.data, passwd)

class EditProfilForm(FlaskForm):
    pseudo = StringField('Pseudo')
    nom = StringField('Nom')
    prenom = StringField('Prenom')
    password = PasswordField('Password')

    def edit_profil(self, user: User) -> None:
        # update user
        if self.pseudo.data != "":
            user.pseudo = self.pseudo.data
        if self.nom.data != "":
            user.nom = self.nom.data
        if self.prenom.data != "":
            user.prenom = self.prenom.data
        if self.password.data != "":
            m = sha256()
            m.update(self.password.data.encode())
            passwd = m.hexdigest()
            user.password = passwd
        UserDB.update_user(user)

class PostForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    contenu = TextAreaField('Contenu', validators=[DataRequired()])

    def create_post(self, user: User) -> None:
        id = PostDB.get_max_id()
        if id is None:
            id = -1
        PostDB.insert_new_post(id+1, self.titre.data, self.contenu.data, datetime.datetime.now(), user)

class SearchForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])

    def search_post_by_titre(self) -> list:
        return PostDB.search_all_posts_by_titre(self.titre.data)
