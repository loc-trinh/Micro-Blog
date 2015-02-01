#!flask/bin/python
import os
from app import app
from flask.ext.script import Manager

from app import db
from app.models import User

manager = Manager(app)

@manager.command
def adduser(email, username, admin=False):
	"""Register a new user."""
	from getpass import getpass
	password = getpass()
	password2 = getpass(prompt='Confirm: ')
	if password != password2:
		import sys
		sys.exit('Error: passwords do not match:')
	db.create_all()
	user = User(email=email, username=username, password=password, is_admin=admin)
	db.session.add(user)
	db.session.commit()
	print('User {0} was registered sucessfully'.format(username))
	
if __name__ == '__main__':
	manager.run()