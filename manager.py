from flask_migrate import  MigrateCommand
from flask_script import Manager
from app import app
from app.models import User,Edit


manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
