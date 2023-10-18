from ..app import login_manager
from .User import User

@login_manager.user_loader
def load_user(id) -> User:
    return User.query.get(id)