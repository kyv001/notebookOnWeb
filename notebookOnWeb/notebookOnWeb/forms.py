from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired

class loginForm(FlaskForm):
    username = StringField(
        "用户名：",
        validators=[
            Length(min=2,max=10,message="请输入2~10个字符长度的用户名"),
            DataRequired(message="用户名不能为空！")
        ]
    )
    userpass = PasswordField(
        "密码：",
        validators=[
            Length(min=4,max=12,message="请输入4~12个字符长度的密码"),
            DataRequired(message="密码不能为空！")
        ]
    )
    submit = SubmitField("登录")
