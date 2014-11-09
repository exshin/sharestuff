#!/usr/bin/python27
#-*- coding: utf-8 -*-

import os
from psycopg2 import connect,extras
from ..configs.config import connStr
from ..db.queries import *


def add_new_user(new_user_data):
	# connect to db and insert new user (check to make sure email doesn't already exist)
	conn = connect(connStr['sharestuff'])
	cursor = conn.cursor()
	print 'add_new_user function: ',new_user_data
	new_user_insert = [new_user_data['username'],
		new_user_data['email'],
		None,
		new_user_data['first_name'],
		new_user_data['last_name'],
		new_user_data['password'],
		None,
		new_user_data['email'],
		new_user_data['username']]
	cursor.execute(sql_insert_new_users,new_user_insert)
	results = cursor.fetchall()
	conn.commit()
	conn.close()
	print 'insert new user results: ', str(results)
	return results