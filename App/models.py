from .app import db

import datetime

class User(db.Model):
    __tablename__ = 'USER'

    pseudo = db.Column(db.Text, primary_key=True)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, pseudo, nom, prenom, email, password):
        self.pseudo = pseudo
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password

class Post(db.Model):
    __tablename__ = 'POST'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text)
    contenu = db.Column(db.Text)
    date = db.Column(db.Date)
    user_pseudo = db.Column(db.Text, db.ForeignKey('USER.pseudo'))

    def __init__(self, titre, contenu, date, user_pseudo):
        self.titre = titre
        self.contenu = contenu
        self.date = date
        self.user_pseudo = user_pseudo
    
    def __repr__(self):
        return '<Post %r>' % self.titre

class APoster(db.Model):
    __tablename__ = 'APOSTER'

    user_pseudo = db.Column(db.Text, db.ForeignKey('USER.pseudo'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('POST.id'), primary_key=True)
    date = db.Column(db.Date)

    def __init__(self, user_pseudo, post_id, date=datetime.date.today()):
        self.user_pseudo = user_pseudo
        self.post_id = post_id
        self.date = date
