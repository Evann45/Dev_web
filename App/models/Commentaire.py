from ..app import db
from .User import User
from .Post import Post

class Commentaire(db.Model):
    __tablename__ = 'COMMENTAIRE'

    id_commentaire = db.Column(db.Integer, primary_key=True)
    email_user = db.Column(db.Text, db.ForeignKey('USER.email'))
    id_post = db.Column(db.Integer, db.ForeignKey('POST.id'))
    texte = db.Column(db.Text)

    def __init__(self, email_user, id_post, texte):
        self.id_commentaire = 0 if db.session.query(db.func.max(Commentaire.id_commentaire)).scalar() is None else db.session.query(db.func.max(Commentaire.id_commentaire)).scalar() + 1
        self.email_user = email_user
        self.id_post = id_post
        self.texte = texte

    # les getteurs
    def get_id_commentaire(self) -> int:
        return self.id_commentaire

    def get_email_user(self) -> str:
        return self.email_user

    def get_id_post(self) -> int:
        return self.id_post

    def get_texte(self) -> str:
        return self.texte

class CommentaireDB:
    @classmethod
    def insert_new_commentaire(cls: Commentaire, email_user: str, id_post: int, texte: str) -> None:
        new_commentaire = Commentaire(email_user, id_post, texte)
        db.session.add(new_commentaire)
        db.session.commit()
    
    @classmethod
    def get_commentaires_by_user(cls: Commentaire, user: User) -> list:
        return Commentaire.query.filter_by(email_user=user.get_email()).all()

    @classmethod
    def get_commentaires_by_post(cls: Commentaire, post: Post) -> list:
        return Commentaire.query.filter_by(id_post=post.get_id()).all()
    
    @classmethod
    def delete_commentaire_by_id(cls: Commentaire, id: int) -> None:
        Commentaire.query.filter_by(id_commentaire=id).delete()
        db.session.commit()