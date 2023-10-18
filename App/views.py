from .app import app
from flask import redirect, render_template, url_for, request, flash
from .models.User import UserDB, User
from .models.Post import PostDB, Post
from .models.LoginManager import load_user
from .Form import LoginForm, RegisterForm, EditProfilForm, PostForm, SearchForm

from flask_login import login_user, current_user, logout_user, login_required

import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('recherche', titre=form.titre.data))
    posts = PostDB.get_all_posts()
    return render_template('home.html', posts=posts, UserDB=UserDB, form=form)

@app.route('/recherche/<titre>', methods=['GET', 'POST'])
def recherche(titre):
    form = SearchForm()
    posts = PostDB.search_all_posts_by_titre(titre)
    if form.validate_on_submit():
        return render_template('home.html', posts=posts, UserDB=UserDB, form=form)
    return render_template('home.html', posts=posts, UserDB=UserDB, form=form)

@app.route('/supprimer_post/<int:id>')
@login_required
def supprimer_post(id):
    PostDB.delete_post_by_id(id)
    return redirect(url_for('mes_posts'))

@app.route('/creer_post', methods=['GET', 'POST'])
@login_required
def creer_post():
    form = PostForm()
    if form.validate_on_submit():
        form.create_post(current_user)
        return redirect(url_for('mes_posts'))
    return render_template('creer_post.html', form=form, title='Créer un post')

@app.route('/mes_posts')
@login_required
def mes_posts():
    posts = PostDB.get_all_posts_by_user(current_user)
    return render_template('mes_posts.html', posts=posts, title='Mes posts')

@app.route('/edit_profil', methods=['GET', 'POST'])
@login_required
def edit_profil():
    form = EditProfilForm()
    if form.validate_on_submit():
        form.edit_profil(current_user)
        flash('Votre profil a été modifié !')
        return redirect(url_for('profil'))
    return render_template('edit_profil.html', form=form, title='Modifier le profil')

@app.route('/profil')
@login_required
def profil():
    return render_template('profil.html')

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
    if not form.is_submitted():
        form.next.data = request.args.get('next')
    elif form.validate_on_submit():
        user = form.get_authenticated_user()
        if user is not None:
            login_user(user)
            next = form.next.data or url_for('home')
            return redirect(next)
        return render_template('login.html', title='Se connecter', form=form)
    return render_template('login.html', title='Se connecter', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if UserDB.get_user_by_email(form.email.data) is not None:
            flash('Email déjà utilisé')
            return render_template('register.html', title='Register', form=form)
        if UserDB.get_user_by_pseudo(form.pseudo.data) is not None:
            flash('Pseudo déjà utilisé')
            return render_template('register.html', title='Register', form=form)
        form.create_account()
        flash('Votre compte a été créé !')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
