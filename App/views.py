from .app import app
from flask import redirect, render_template, url_for, request, flash
from .models.User import UserDB, User
from .models.Post import PostDB, Post
from .models.LoginManager import load_user
from .Form import LoginForm

from flask_login import login_user, current_user, logout_user

import datetime

@app.route('/home')
def home():
    flash(current_user)
    return render_template('home.html')

@app.route('/test')
def posts():
    UserDB.insert_new_user("email1@gmail.com", "pseudo", "nom", "prenom", "password")
    UserDB.insert_new_user("email2@gmail.com", "pseudo1", "nom", "prenom", "password")
    UserDB.insert_new_user("email3@gmail.com", "pseudo2", "nom", "prenom", "password")
    UserDB.insert_new_user("email4@gmail.com", "pseudo3", "nom", "prenom", "password")
    PostDB.insert_new_post(1, "titre", "c1", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(2, "titre", "c2", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(3, "titre", "c3", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(4, "titre", "c4", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(5, "titre", "c5", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    posts = PostDB.get_all_posts()
    return render_template('test.html', posts=posts, user=UserDB.get_user_by_email("email1@gmail.com"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.get_authenticated_user()
        if user is not None:
            login_user(user)
            return redirect(url_for("home"))
        return render_template('login.html', title='Se connecter', form=form)
    return render_template('login.html', title='Se connecter', form=form)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('login'))
