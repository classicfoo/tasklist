#!/usr/bin/env python3
from datetime import date 
from datetime import datetime
import argparse
import sqlite3

#add command arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", action="store_true", help="add a new task")
args = parser.parse_args()

#add database
conn = sqlite3.connect('tasklist.db')
c = conn.cursor()

#setup tables
c.execute('''CREATE TABLE IF NOT EXISTS tasks 
		(int id, boolean done, datetime done, text title)''')

class Task:

	id = 0
	done = False
	due = date.today()
	title = "untitled"

	def __init__(self, id, done = False, due = date.today().strftime("%d/%m/%y"), title = "untitled"):
		self.id = id
<<<<<<< HEAD
		self.done = done
		self.due = due 
		self.title = title

	def display(self):
		print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(self.id, self.done, self.due, self.title))
=======

	def display(self):
		print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(self.id, self.done, self.due.strftime("%d/%m/%y"), self.title))
>>>>>>> 13f0e7ac888685e8e13432d53ae297b514ce3f01

class Tasks:
	
	tasks = []

#	def __init__(self):
#		id = len(self.tasks)
#		self.tasks.append(Task(id)) 	

<<<<<<< HEAD
	def add(self, task=Task(0)):
		self.tasks.append(task)	
		return task

	def addrange(self, *rows):
		if (len(rows[0]) > 0) and (len(rows) > 0):
			for r in rows:
				for t in r:
					self.add(Task(t[0],t[1],t[2],t[3]))

	def display(self):
		for t in self.tasks:
			t.display()

	def count(self):
		return len(self.tasks)
=======
	def add(self):
		id = len(self.tasks)
		self.tasks.append(Task(id))	
		
	def display(self):
		for t in self.tasks:
			t.display()
>>>>>>> 13f0e7ac888685e8e13432d53ae297b514ce3f01

tasklist = Tasks()

#load existing tasks from database
c.execute("SELECT * FROM tasks")
rows = c.fetchall()
tasklist.addrange(rows)

#add new task
if args.add:
	id = tasklist.count()
	t = tasklist.add(Task(id)) #task
	tt = (t.id, t.done, t.due, t.title) #task tuple
	c.execute("INSERT INTO tasks VALUES (?,?,?,?)",tt)
	conn.commit()

#print out all tasks
<<<<<<< HEAD
tasklist.display()
=======
tasks.display()
>>>>>>> 13f0e7ac888685e8e13432d53ae297b514ce3f01

conn.close()	
