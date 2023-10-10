import click

from .app import app, db

@app.cli.command()
def initdb():
    """Initialise la base de données"""
    print('Init the db')
    db.create_all()
    print('Done')