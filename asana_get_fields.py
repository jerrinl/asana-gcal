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
	Validates Asana access token. 
	TODO: upload token to Github and have it used there instead of as environ variable
	"""
	if 'ASANA_ACCESS_TOKEN' in os.environ:
		client = asana.Client.oauth(
			client_id=os.environ['ASANA_CLIENT_ID'],
			client_secret=os.environ['ASANA_CLIENT_SECRET'],
			# this special redirect URI will prompt the user to copy/paste the code.
			# useful for command line scripts and other non-web apps
			redirect_uri='urn:ietf:wg:oauth:2.0:oob'
		)
		
		return client
	else: 
		raise Exception("Could not establish Asana Oauth connection."
		
		

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
	
	workspace_id = me['workspaces'][0]['id]
	
	proj_custom_fields = client.custom_fields.
	
	
		
def main():
	
	if validate_asana_session()
	 
	 
	