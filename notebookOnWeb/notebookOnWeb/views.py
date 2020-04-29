from flask import \
    render_template,\
    redirect,\
    url_for,\
    session
import sqlite3
from notebookOnWeb.forms import *
from notebookOnWeb import app
import hashlib

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
except Exception as e:print(e)
try:
    cursor.execute(
        """
        CREATE TABLE notes(
            topic   CHAR(20)    NOT NULL,
            name    CHAR(10)    NOT NULL,
            note    CHAR(1000)   NOT NULL,
            public  INTEGER     NOT NULL
        );
        """
    )
    conn.commit()
except Exception as e:print(e)

@app.route('/home')
def home():
    cursor.execute("SELECT topic FROM notes WHERE name=? OR public=1",(session.get('usr'),))
    topics = list(set(cursor.fetchall()))
    return render_template(
        'index.html',
        usr=session.get('usr'),
        topics=topics
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
        if res[0] == hashlib.md5(bytes(loginform.userpass.data,encoding='utf-8')).hexdigest():
            session['usr'] = loginform.username.data
            return redirect(url_for("home"))
        else:
            return render_template('login.html',
                                   title='用户名或密码错误，请重新登陆',
                                   form=loginform,
                                   usr=session.get('usr'))
    return render_template('login.html',
                           title='登录',
                           form=loginform,
                           usr=session.get('usr'))

@app.route('/edit',methods=['GET','POST'])
def edit():
    editform = editForm()
    if not session.get('usr'):
        return redirect(url_for("login"))
    if editform.validate_on_submit():
        cursor.execute("INSERT INTO notes VALUES (?,?,?,?)",(
            editform.topic.data,
            session['usr'],
            editform.note.data,
            editform.public.data))
        conn.commit()
        return redirect(url_for("home"))
    return render_template('editnotes.html',
                           title='写下你的想法',
                           form=editform,
                           usr=session.get('usr'))

@app.route('/logon',methods=['GET','POST'])
def logon():
    logonform = logonForm()
    if logonform.validate_on_submit():
        cursor.execute("SELECT pswdhash FROM users WHERE name = ?",
                          (logonform.username.data,))
        if cursor.fetchone():
            return render_template('logon.html',
                                   title='用户名已存在',
                                   form=logonform,
                                   usr=session.get('usr'))
        cursor.execute("INSERT INTO users VALUES (?,?)",(
            logonform.username.data,
            hashlib.md5(bytes(logonform.userpass.data,encoding='utf-8')).hexdigest()))
        conn.commit()
        session['usr'] = logonform.username.data
        return redirect(url_for("home"))
    return render_template('logon.html',
                           title='注册',
                           form=logonform,
                           usr=session.get('usr'))

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('usr',None)
    return redirect(url_for('home'))

@app.route('/shownotes/<topic>')
def shownotes(topic):
    cursor.execute("SELECT name,note FROM notes WHERE topic=? AND (name=? OR public=1)",
                   (topic,session.get('usr')))
    notes = cursor.fetchall()
    return render_template('shownotes.html',
                           title='主题为{}的笔记'.format(topic),
                           notes=notes,
                           usr=session.get('usr'))
