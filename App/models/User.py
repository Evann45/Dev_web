from ..app import db

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
    
    def __repr__(self):
        return '<User %r>' % self.pseudo