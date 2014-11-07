#!/usr/bin/python27
#-*- coding: utf-8 -*-

from psycopg2 import connect,extras



def add_new_user():
	# connect to db and insert new user (check to make sure email doesn't already exist)
	return None