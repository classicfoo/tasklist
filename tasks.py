#!/usr/bin/env python3
from datetime import date 
import argparse

#add command arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", action="store_true", help="add a new task")
args = parser.parse_args()

class Task:

	id = 0
	done = False
	title = "untitled"
	due = date.today()

	def __init__(self, id):
		self.id = id

	def display(self):
		print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(self.id, self.done, self.due.strftime("%d/%m/%y"), self.title))

class Tasks:
	
	tasks = []

	def __init__(self):
		id = len(self.tasks)
		self.tasks.append(Task(id)) 	

	def add(self):
		id = len(self.tasks)
		self.tasks.append(Task(id))	
		
	def display(self):
		for t in self.tasks:
			t.display()

tasks = Tasks()

#add new task
if args.add:
	tasks.add()

#print out all tasks
tasks.display()

	
