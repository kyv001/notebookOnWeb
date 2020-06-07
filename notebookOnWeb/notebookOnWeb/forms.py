from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Length,DataRequired,EqualTo

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

class logonForm(FlaskForm):
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
    passagain = PasswordField(
        "重新输入密码：",
        validators=[
            Length(min=4,max=12,message="请输入4~12个字符长度的密码"),
            DataRequired(message="密码不能为空！"),
            EqualTo("userpass","两次密码不同！")
        ]
    )
    submit = SubmitField("注册")

class editForm(FlaskForm):
    topic = StringField(
        "主题",
        validators=[
            Length(min=1,max=20,message="主题不能大于20字！"),
            DataRequired(message="不能上传空主题！")
        ]
    )
    note = TextAreaField(
        "正文",
        validators=[
            Length(min=1,max=20000,message="笔记不能大于20000字！"),
            DataRequired(message="不能上传空笔记！")
        ]
    )
    public = RadioField('是否对别人可见？', choices=[('1', '是'), ('0', '否')],
                                  validators=[DataRequired("请选择！")])
    submit = SubmitField("上传")
