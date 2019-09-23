# from flaskext.markdown import Markdown
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()
def create_init(app):
    db.init_app(app)
    migrate =Migrate()
    migrate.init_app(app,db)
    session =Session()
    session.init_app(app)
