from ..app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'USER'

    email = db.Column(db.Text, primary_key=True)
    pseudo = db.Column(db.Text)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, email, pseudo, nom, prenom, password):
        self.email = email
        self.pseudo = pseudo
        self.nom = nom
        self.prenom = prenom
        self.password = password

    # les getteurs
    def get_id(self):
           return (self.email)

    def get_pseudo(self) -> str:
        return self.pseudo

    def get_nom(self) -> str:
        return self.nom
    
    def get_prenom(self) -> str:
        return self.prenom
    
    def get_email(self) -> str:
        return self.email
    
    def get_password(self) -> str:
        return self.password
    
class UserDB:
    @classmethod
    def insert_new_user(cls: User, email: str, pseudo: str, nom: str, prenom: str, password: str) -> None:
        new_user = User(email, pseudo, nom, prenom, password)
        db.session.add(new_user)
        db.session.commit()
    
    @classmethod
    def get_user_by_email(cls: User, email: str) -> User:
        return User.query.get(email)

    @classmethod
    def get_user_by_pseudo(cls: User, pseudo: str) -> User:
        return User.query.filter_by(pseudo=pseudo).first()
    
    @classmethod
    def update_user(cls: User, user: User) -> None:
        db.session.commit()
