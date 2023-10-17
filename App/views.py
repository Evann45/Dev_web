from .app import app
from flask import render_template
from .models.User import UserDB
from .models.Post import PostDB
import datetime

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/posts')
def posts():
    UserDB.insert_new_user("pseudo", "nom", "prenom", "email", "password")
    PostDB.insert_new_post(1, "titre", "c1", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(2, "titre", "c2", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(3, "titre", "c3", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(4, "titre", "c4", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    PostDB.insert_new_post(5, "titre", "c5", datetime.datetime.now(), UserDB.get_user_by_pseudo("pseudo"))
    posts = PostDB.get_all_posts()
    return render_template('test.html', posts=posts)