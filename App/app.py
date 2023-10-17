from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

import os.path

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.getcwd())+"/App/data/blog.db"
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '67ca4656-dded-4305-b5b8-7992cc0c2119'
login_manager = LoginManager(app)