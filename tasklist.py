#!/usr/bin/env python3
from datetime import date 
from datetime import datetime
#import argparse
import sqlite3

##add command arguments 
#parser = argparse.ArgumentParser()
#parser.add_argument("-a", "--add", action="store_true", help="add a new task")
#args = parser.parse_args()

tasklist = []

def initialize_database():
	#add database
	conn = sqlite3.connect('tasklist.db')
	c = conn.cursor()

	#setup tables
	c.execute('''CREATE TABLE IF NOT EXISTS tasks 
			(int id, boolean done, datetime done, text title)''')

	#close database
	conn.close()	


def create_task(id, done = False, due = date.today().strftime("%d/%m/%y"), title = "untitled"):
	return (id, done, due, title)

def print_task(t):
	print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(t[0],t[1],t[2],t[3]))

def print_tasklist():
	for t in tasklist:
		print_task(t)

def add_task(t):
	tasklist.append(t)
	save_task(t)

def load_tasklist():
	#add database
	conn = sqlite3.connect('tasklist.db')
	c = conn.cursor()

	#load existing tasks from database
	c.execute("SELECT * FROM tasks")
	rows = c.fetchall()
	for r in rows:
		tasklist.append(r)

	#close database
	conn.close()	

def save_task(t):
	#add database
	conn = sqlite3.connect('tasklist.db')
	c = conn.cursor()
	
	#insert tasks into database
	c.execute("INSERT INTO tasks VALUES (?,?,?,?)",t)
	conn.commit()

	#close database
	conn.close()	

load_tasklist()


#initialize_database()
#
#load_tasklist()
#
#if args.add:
#	id = len(tasklist) 
#	task = create_task(id)
#	save_task(task)
#
#print_tasklist()
#
#close_database()
