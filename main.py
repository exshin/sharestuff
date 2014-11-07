#!/usr/bin/python27
#-*- coding: utf-8 -*-

import os
import requests
from flask import Flask, make_response, render_template, request, jsonify
from flask import send_from_directory, session, url_for, redirect
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/shared')
def shared():
    return render_template('shared.html')

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

app.secret_key = 'A0Zr80j/3yX r~XHH!jmN]L^X/,?RT'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)



