from flask import \
    render_template,\
    redirect,\
    url_for,\
    session
import sqlite3
from notebookOnWeb.forms import *
from notebookOnWeb import app

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
        session['usr'] = loginform.username.data
        return redirect(url_for("home"))
    return render_template('login.html',title='登录',form=loginform)

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('usr',None)
    return redirect(url_for('home'))
