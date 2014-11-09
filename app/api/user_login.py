#!/usr/bin/python27
#-*- coding: utf-8 -*-

import os
from psycopg2 import connect,extras
from ..configs.config import connStr
from ..db.queries import *

def get_password_hash(username):
	# get hashed password in db
	conn = connect(connStr['sharestuff'])
	cursor = conn.cursor()
	cursor.execute('SELECT DISTINCT user_password FROM users WHERE user_name = %s',[username])
	password = cursor.fetchone()
	if password:
		return password[0]
	else:
		return None

def get_user_data(username):
	# get hashed password in db
	conn = connect(connStr['sharestuff'])
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE user_name = %s',[username])
	user_data = cursor.fetchone()
	if user_data:
		print user_data
		return user_data
	else:
		return None