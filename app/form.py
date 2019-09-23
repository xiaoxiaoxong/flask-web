from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, EqualTo, length


class Loginform(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired('用户名不能为空')],
                           render_kw={'class': 'form-control', 'plaaceholder': '用户名'})
    password = PasswordField('密 码:', validators=[DataRequired('密码不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '密码'})


class Registform(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired('用户名不能为空')],
                           render_kw={'class': 'form-control', 'plaaceholder': '用户名'})
    password = PasswordField('密 码:', validators=[DataRequired('密码不能为空')],
                             render_kw={'class': 'form-control', 'placeholder': '密码'})
    password2 = PasswordField('再次输入密码:', validators=[DataRequired('密码不能为空'),EqualTo('password')],
                             render_kw={'class': 'form-control', 'placeholder': '再次输入密码'})

class  Wendaform(FlaskForm):
    title = StringField('标题',validators=[DataRequired()],render_kw={'class':'wendaform'})
    content = TextAreaField('内容',validators=[DataRequired()],render_kw={'class':'wendacontent'})

class PostForm(FlaskForm):
    title = StringField('标题:',validators=[DataRequired(),length(max=255)])
    content = TextAreaField('内容:',validators=[DataRequired()])

