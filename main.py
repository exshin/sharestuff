#!/usr/bin/python27
#-*- coding: utf-8 -*-

import os
import requests
import ast
from flask import Flask, make_response, render_template, request, jsonify
from flask import send_from_directory, session, url_for, redirect
from flask.ext import admin, login
from werkzeug.security import generate_password_hash, check_password_hash

import json

from app.api.new_user import *
from app.api.user_login import *
from app.api.items import *


app = Flask(__name__)

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    if session.get('logged_in'):
        return redirect(url_for('browse'))
    else:
        return render_template('home.html')

@app.route('/browse')
def browse():
    if session.get('logged_in'):
        items = get_all_items()
        return render_template('browse.html', user_firstname=session.get('user_firstname'), items=items)
    else:
        return redirect("/index", code=302)

@app.route('/shared')
def shared():
    if session.get('logged_in'):
        userid = session.get('userid')
        items = get_items(userid)
        return render_template('shared.html', user_firstname=session.get('user_firstname'), items=items)
    else:
        return redirect("/index", code=302)

@app.route('/borrowed')
def borrowed():
    return render_template('borrowed.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/api/new_user', methods=['GET','POST'])
def new_user():
    # add new user to db
    if request.method == 'POST':
        new_user_data = ast.literal_eval(json.dumps(request.form, separators=(',',':')))
        print new_user_data
        if new_user_data:
            # insert user data
            new_user_data['password'] = generate_password_hash(new_user_data['password'])
            new_user_id = add_new_user(new_user_data)
            if new_user_id:
                return 'success'
            else:
                return 'fail'

@app.route('/api/new_item', methods=['GET','POST'])
def new_item():
    # add new item to db
    if request.method == 'POST':
        new_item_data = ast.literal_eval(json.dumps(request.form, separators=(',',':')))
        print new_item_data
        if new_item_data:
            # insert item data
            new_item_data['item_owner_id'] = session.get('userid')
            new_item_data['item_owner_name'] = session.get('username')
            new_item_id = add_new_item(new_item_data)
            if new_item_id:
                return 'success'
            else:
                return 'fail'

@app.route('/login', methods=['GET','POST'])
def login_view():
    # handle user login
    login_data = ast.literal_eval(json.dumps(request.form, separators=(',',':')))
    username = login_data['username']
    password = login_data['password']
    print username,password

    # we're comparing the plaintext pw with the the hash from the db
    user_data_db = get_user_data(username)
    password_hash = None
    if user_data_db:
        password_hash = user_data_db[3]
    if not check_password_hash(password_hash, password):
        print password, ' does not match password hash from db'
        return 'fail'
        # raise password error (do not log in)
    else:
        print 'Redirecting to /browse'
        session['logged_in'] = True
        session['username'] = username
        session['user_firstname'] = user_data_db[5]
        session['user_lastname'] = user_data_db[6]
        session['user_email'] = user_data_db[2]
        session['user_avatar'] = user_data_db[8]
        session['userid'] = user_data_db[0]
        return 'success'
    

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/clear_sessions')
def clear_sessions():
    session.clear()
    return """
        <p>Logged out</p>
        <p><a href="/movie_poll">Return to Movie Poll</a></p>
        """ 

@app.route('/logout')
def logout():
    session.clear()
    return """
        <p>Logged out</p>
        <p><a href="/">Return to Home</a></p>
        """ 

app.secret_key = 'A0Zr80j/3yX r~XHH!jnN]L^X/,?RT'

# Initialize flask-login
init_login()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)
    login_manager.init_app(app)



