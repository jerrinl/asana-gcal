from __future__ import print_function
import os
import sys 
from six import print_
import json
import asana
import datetime


def validate_asana_session():
	"""
	Validates Asana using a Personal Access Token
	TODO: Oauth setup instead

	args:
		none
	return:
		client; allows any sort of interface w/ Asana
	"""
	client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])

	return client
	
def get_user_project_fields(client):
	"""
	Get user's project that we are looking for the custom fields in.
	Naive implementation - just get the client and explicitly look for the Asana Inc org
	followed by the project that literally says 'CF' 
	"""
	
	# projects = client.projects.find_all({'choice_workspace': workspace['id']})

	user_fields = client.workspaces.workspace_id('15793206719').custom_fields

	return user_fields


	
	
		
def main():

	# PAT: '0/7b5e3d4a15cc16050e3f29f31d2085fd'
	# workspace ID : 15793206719 // 'Asana, Inc'
	# project ID: 215978128317963 // 
	# task ID: 215978128317964

	client = validate_asana_session()
	get_user_project_fields(client)
	

		 
	 
if __name__ == '__main__':
	main()