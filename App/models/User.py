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

    # les getteurs
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
    def insert_new_user(cls: User, pseudo: str, nom: str, prenom: str, email: str, password: str) -> None:
        new_user = User(pseudo, nom, prenom, email, password)
        db.session.add(new_user)
        db.session.commit()
    
    @classmethod
    def get_user_by_pseudo(cls: User, pseudo: str) -> User:
        return User.query.filter_by(pseudo=pseudo).first()