from ..app import db

class Post(db.Model):
    __tablename__ = 'POST'

    id = db.Column(db.Integer, primary_key=True)
    user_pseudo = db.Column(db.Text, db.ForeignKey('USER.pseudo'), primary_key=True)
    titre = db.Column(db.Text)
    contenu = db.Column(db.Text)
    date = db.Column(db.Date)

    def __init__(self, titre, contenu, date, user_pseudo):
        self.titre = titre
        self.contenu = contenu
        self.date = date
        self.user_pseudo = user_pseudo
    
    def __repr__(self):
        return '<Post %r>' % self.titre