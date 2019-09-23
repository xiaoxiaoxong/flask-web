from flask import Flask

from app.admin import init_admin
from app.exts import create_init

from app.home import init_home
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY']= os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/answer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_admin(app)
init_home(app)
create_init(app)