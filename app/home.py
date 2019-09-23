from flask import Blueprint, render_template, request, flash, redirect, session, url_for, g
from werkzeug.security import generate_password_hash
import markdown
from app.exts import db
from app.form import Loginform, Registform, Wendaform, PostForm
from app.models import User, Edit
from app.setting import login_required

home = Blueprint('home',__name__)
def init_home(app):
    app.register_blueprint(blueprint=home)


@home.route('/')
def index():
    edit = Edit.query.order_by(Edit.datetime.desc()).all()

    return render_template('index.html',edit =edit)

@home.route('/search/')
def search():
    search = request.args.get('search')
    edit = Edit.query.filter(Edit.title.contains(search)).all()
    return render_template('index.html', edit=edit)


@home.route('/login/', methods=['GET','POST'])
def login():
    form = Loginform()
    if request.method == 'GET':
        return render_template('login.html',form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        passwd= user.check_password(password)
        if passwd:
            session['user_id'] = user.id
            return redirect(url_for('home.index'))
        else:
            flash(u'密码错误')
            return render_template('login.html',form=form)

@home.route('/regist/',methods=['GET','POST'])
def regist():
    form = Registform()
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]):
            flash(u'不能为空')
        elif password != password2:
            flash(u'密码不一致')
        else:
            user = User(username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash(u'恭喜{}，注册成功'.format(username))
    return render_template('register.html',form=form)

@home.route('/Personal/')
def Personal():
    return render_template('personal.html')


@home.context_processor
def my_context_processor():
    if hasattr(g,'user'):
        return {'user':g.user}
    return {}
@home.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('home.login'))

@home.before_request
def my_before_request():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    g.user = user


@home.route('/wenda/',methods= ['GET','POST'])
@login_required
def wenda():
    form = PostForm()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = g.user.id
        edit = Edit(title=title,content=content,user_id=user_id)
        db.session.add(edit)
        db.session.commit()
        id =edit.id
        return redirect(url_for('home.wendapost',id =id ))
    return render_template('testmkd.html',form=form)
@home.route('/wendapost/<int:id>')
def wendapost(id):
    edit = Edit.query.filter(Edit.id==id).first()
    html = markdown.markdown(edit.content,output_format='html')
    content = {
        'title':edit.title,
        'datetime':edit.datetime,
        'user':edit.user.username,
        'text':html
    }
    return  render_template('wendapost.html',content=content)


@home.route('/deletedata/')
def deletedata():
    edit = Edit.query.filter(Edit.user_id == g.user.id).all()
    for s in edit:
        db.session.delete(s)
        db.session.commit()
    return render_template('personal.html', edit=edit)
