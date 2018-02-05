from app import app, db
from app.models import User, Post

@app.shell_context_processor #  this fungtion is to make `flask shell` work
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}