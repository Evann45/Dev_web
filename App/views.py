from .app import app
from flask import redirect, render_template, url_for, request, flash
from .models.User import UserDB
from .models.Post import PostDB
from .models.Commentaire import CommentaireDB
from .models.LoginManager import load_user
from .Form import LoginForm, RegisterForm, EditProfilForm, PostForm, SearchForm, CommentaireForm

from flask_login import login_user, current_user, logout_user, login_required

import datetime, timeago

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    sForm = SearchForm()
    if sForm.validate_on_submit():
        return redirect(url_for('recherche', titre=sForm.titre.data))
    posts = PostDB.get_all_posts()
    return render_template('home.html', posts=posts, UserDB=UserDB, sForm=sForm, timeago=timeago, datetime=datetime)

@app.route('/supprimer_commentaire/<int:id>/<int:id_comm>')
@login_required
def supprimer_commentaire(id, id_comm):
    CommentaireDB.delete_commentaire_by_id(id_comm)
    return redirect(url_for('post', id=id))

@app.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    form = CommentaireForm()
    sForm = SearchForm()
    if form.validate_on_submit():
        form.create_commentaire(current_user, id)
        return redirect(url_for('post', id=id))
    post = PostDB.get_post_by_id(id)
    return render_template('post.html', post=post, commentaires=CommentaireDB.get_commentaires_by_post(post), UserDB=UserDB, form=form, timeago=timeago, datetime=datetime, sForm=sForm)

@app.route('/recherche/<titre>', methods=['GET', 'POST'])
def recherche(titre):
    sForm = SearchForm()
    posts = PostDB.search_all_posts_by_titre(titre)
    if sForm.validate_on_submit():
        return render_template('home.html', posts=posts, UserDB=UserDB, sForm=sForm, timeago=timeago, datetime=datetime)
    return render_template('home.html', posts=posts, UserDB=UserDB, sForm=sForm, timeago=timeago, datetime=datetime)

@app.route('/supprimer_post/<int:id>')
@login_required
def supprimer_post(id):
    PostDB.delete_post_by_id(id)
    CommentaireDB.delete_commentaire_by_post_id(id)
    return redirect(url_for('mes_posts'))

@app.route('/creer_post', methods=['GET', 'POST'])
@login_required
def creer_post():
    form = PostForm()
    sForm = SearchForm()
    if form.validate_on_submit():
        form.create_post(current_user)
        return redirect(url_for('mes_posts'))
    return render_template('creer_post.html', form=form, title='Créer un post', sForm=sForm)

@app.route('/mes_posts')
@login_required
def mes_posts():
    posts = PostDB.get_all_posts_by_user(current_user)
    sForm = SearchForm()
    return render_template('mes_posts.html', posts=posts, title='Mes posts', timeago=timeago, datetime=datetime, sForm=sForm)

@app.route('/edit_profil', methods=['GET', 'POST'])
@login_required
def edit_profil():
    form = EditProfilForm()
    sForm = SearchForm()
    if form.validate_on_submit():
        form.edit_profil(current_user)
        flash('Votre profil a été modifié !')
        return redirect(url_for('profil'))
    return render_template('edit_profil.html', form=form, title='Modifier le profil', sForm=sForm)

@app.route('/profil')
@login_required
def profil():
    sForm = SearchForm()
    return render_template('profil.html', title='Profil', sForm=sForm)

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
            next = form.next.data
            if next is None or next == "":
                next = url_for('home')
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
