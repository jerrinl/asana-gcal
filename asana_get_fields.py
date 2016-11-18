from __future__ import print_function
import httplib2
import os
import sys 
import json
import asana
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
		

def validate_asana_session():
	"""
	Validates Asana using a Personal Access Token
	Creates a client wih Personal Access Client
	TODO: Oauth setup instead

	args:
		none
	return:
		client; allows any sort of interface w/ Asana
	"""
	client = asana.Client.access_token('0/7b5e3d4a15cc16050e3f29f31d2085fd')

	return client
	
def get_user_project(client):
	"""
	Get user's project that we are looking for the custom fields in.
	Naive implementation - just get the client and explicitly look for the Asana Inc org
	followed by the project that literally says 'CF' 
	"""
	me = client.users.me()
	user_workspaces = client.workspaces.


def get_task_data(client):
	"""
	Gets Custom Field data from a task.
	
	args: 
		client - authorized session for Asana account
	return:
		task_data - tuple of time and description
	"""
	me = client.users.me()
	print "Hello " + me['name']
	
		
	
	
		
def main():
	client = validate_asana_session()
	get_task_data(client)
		 
	 
if __name__ == '__main__':
    main()