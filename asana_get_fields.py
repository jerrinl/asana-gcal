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


def main():

	validated_session = validate_asana_session()
	
		

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
		print_("authorized=".client.session.authorized)
		
		(url, state) = client.session.authorization_url()
		
		try:
			import webbrowser
			webbrowser.open(url)
		except Exception as e:
			print_("Open the following URL in a browser to authorize:")
			print_(url)
			