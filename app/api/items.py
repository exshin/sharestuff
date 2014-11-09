#!/usr/bin/python27
#-*- coding: utf-8 -*-

import os
from psycopg2 import connect,extras
from ..configs.config import connStr
from ..db.queries import *


def add_new_item(new_item_data):
	# connect to db and insert new user (check to make sure email doesn't already exist)
	conn = connect(connStr['sharestuff'])
	cursor = conn.cursor()
	print 'add_new_user function: ',new_item_data
	new_item_insert = [new_item_data['item_name'],
		new_item_data['item_description'],
		0, #item_price
		new_item_data['item_image_url'],
		new_item_data['item_category'],
		new_item_data['item_owner_id'],
		new_item_data['item_owner_name'],
		new_item_data['all_can_view']]
	cursor.execute(sql_insert_new_item,new_item_insert)
	results = cursor.fetchall()
	conn.commit()
	conn.close()
	print 'insert new user results: ', str(results)
	return results


def get_items(user_id):
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