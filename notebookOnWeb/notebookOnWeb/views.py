from flask import \
    render_template,\
    redirect,\
    url_for,\
    session
import sqlite3
from notebookOnWeb.forms import *
from notebookOnWeb import app

conn = sqlite3.connect("data.db",check_same_thread=False)
cursor = conn.cursor()

try:
    cursor.execute(
        """
        CREATE TABLE users(
            name        CHAR(10) PRIMARY KEY    NOT NULL,
            pswdhash    CHAR(40)                NOT NULL
        );
        """
    )
    conn.commit()
    cursor.execute(
        """
        CREATE TABLE notes(
            title   CHAR(20)    NOT NULL,
            name    CHAR(10)    NOT NULL,
            note    CHAR(400)   NOT NULL,
            public  INTEGER     NOT NULL
        );
        """
    )
    conn.commit()
except Exception as e:print(e)

@app.route('/home')
def home():
    return render_template(
        'index.html',
        usr=session.get('usr')
    )

@app.route('/')
def toHome(): # go back home
    return redirect(
        url_for('home')
    )

@app.route('/login',methods=['GET','POST'])
def login():
    loginform = loginForm()
    if loginform.validate_on_submit():
        cursor.execute("SELECT pswdhash FROM users WHERE name = ?",(loginform.username.data,))
        res = cursor.fetchone() or [None]
        if res[0] == str(hash(loginform.userpass.data)):
            session['usr'] = loginform.username.data
            return redirect(url_for("home"))
        else:
            return render_template('login.html',title='用户名或密码错误，请重新登陆',form=loginform)
    return render_template('login.html',title='登录',form=loginform)

@app.route('/edit',methods=['GET','POST'])
def edit():
    editform = editForm()
    if not session.get('usr'):
        return redirect(url_for("login"))
    if editform.validate_on_submit():
        cursor.execute("INSERT INTO notes VALUES (?,?,?,?)",(
            editform.title.data,
            session['usr'],
            editform.note.data,
            editform.public.data))
        conn.commit()
        return redirect(url_for("home"))
    return render_template('editnotes.html',title='写下你的想法',form=editform)

@app.route('/logon',methods=['GET','POST'])
def logon():
    logonform = logonForm()
    if logonform.validate_on_submit():
        cursor.execute("SELECT pswdhash FROM users WHERE name = ?",
                          (logonform.username.data,))
        if cursor.fetchone():
            return render_template('logon.html',title='用户名已存在',form=logonform)
        cursor.execute("INSERT INTO users VALUES (?,?)",(
            logonform.username.data,
            hash(logonform.userpass.data)))
        conn.commit()
        session['usr'] = logonform.username.data
        return redirect(url_for("home"))
    return render_template('logon.html',title='注册',form=logonform)

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('usr',None)
    return redirect(url_for('home'))
