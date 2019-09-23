from flask import Blueprint

admin = Blueprint('admin',__name__)
def init_admin(app):
    app.register_blueprint(blueprint=admin)


