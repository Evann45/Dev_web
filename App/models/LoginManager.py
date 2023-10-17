from ..app import login_manager
from .User import User

@login_manager.user_loader
def load_user(user) -> User:
    return user