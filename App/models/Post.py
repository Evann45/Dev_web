from ..app import db
from .User import User

import datetime

class Post(db.Model):
    __tablename__ = 'POST'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text)
    contenu = db.Column(db.Text)
    date = db.Column(db.Date)
    user_mail = db.Column(db.Text, db.ForeignKey('USER.email'))

    def __init__(self, id, titre, contenu, date, user_mail):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.date = date
        self.user_mail = user_mail
    
    # les getteurs
    def get_id(self) -> int:
        return self.id
    
    def get_titre(self) -> str:
        return self.titre
    
    def get_contenu(self) -> str:
        return self.contenu
    
    def get_date(self) -> datetime:
        return self.date
    
    def get_user_mail(self) -> str:
        return self.user_mail

class PostDB:
    @classmethod
    def get_max_id(cls: Post) -> int:
        return db.session.query(db.func.max(Post.id)).scalar()

    @classmethod
    def insert_new_post(cls: Post, id: int, titre: str, contenu: str, date: datetime, user: User) -> None:
        new_post = Post(id, titre, contenu, date, user.get_email())
        db.session.add(new_post)
        db.session.commit()
    
    @classmethod
    def delete_post_by_id(cls: Post, id: int) -> None:
        Post.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def get_post_by_id(cls: Post, id: int) -> Post:
        return Post.query.filter_by(id=id).first()

    @classmethod
    def get_all_posts(cls: Post) -> list:
        return Post.query.all()
    
    @classmethod
    def get_all_posts_by_user(cls: Post, user: User) -> list:
        return Post.query.filter_by(user_mail=user.get_email()).all()