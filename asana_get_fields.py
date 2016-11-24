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
	TODO: Oauth2 setup instead

	args:
		none
	return:
		client; allows any sort of interface w/ Asana
	"""
	client = asana.Client.access_token() 

	return client #keep
	
def get_user_project_fields(client):
	"""
	Get user's project that we are looking for the custom fields in.
	Validates if the project has the necessary fields??
	"""
	
	# projects = client.projects.find_all({'choice_workspace': workspace['id']})
	fields_to_look_for = {	'GCAL_START_TIME_HOUR':0,
							'GCAL_START_TIME_MIN':0,
							'GCAL_END_TIME_HOUR':0,
							'GCAL_END_TIME_MIN':0, 
							'GCAL_AM_OR_PM':0 }
	user_fields = client.custom_field_settings.find_by_project('215978128317963') # TODO: replace this with...not-static value.

	# print(user_fields)
	
	counter = 0
	for i in range(0,len(user_fields)):
		current_field = user_fields[i]["custom_field"]["name"]

		if current_field in fields_to_look_for:
			current_field = get_task_values(this.client,current_field) #nope
	

def get_tasks_from_proj(client,project_id): #keep
	"""
	Given a project ID, get all tasks from the project.
	Assumes the project has valid custom fields?

	args:
		client - auth'd asana session
		project_id - the project you're getting tasks from
	returns:
		task_id_list - a list of task IDs from the project
	"""
	project_tasks = client.tasks.find_by_project(project_id)

	task_id_list = []

	for task in project_tasks:
		task_id_list.append(task['id'])

	return task_id_list




def get_task_data(client,task_id_list): #keep
	"""
	Given a task, retreive the specific custom field value for that task
	calls make_gcal_event ? nah

	"""
	for task_id in task_id_list:
		raw_task = client.tasks.find_by_id(task_id) # iterate through each task in proj, then through each field
		cf_appender_us(raw_task)

def cf_appender_us(raw_task_data):
	"""
	returns a better formatted thing from a task
	"""
	eventData = {	'GCAL_START_TIME_HOUR':0,
					'GCAL_START_TIME_MIN':0,
					'GCAL_END_TIME_HOUR':0,
					'GCAL_END_TIME_MIN':0, 
					'GCAL_AM_OR_PM':''}

	for x in raw_task_data["custom_fields"]:
		if x["name"] in eventData:
			eventData[x["name"]] = x["enum_value"]["name"]

	start_time = eventData["GCAL_START_TIME_HOUR"] + eventData["GCAL_START_TIME_MIN"] + eventData["GCAL_AM_OR_PM"]
	end_time = eventData["GCAL_END_TIME_HOUR"] + eventData["GCAL_END_TIME_MIN"] + eventData["GCAL_AM_OR_PM"]

	
def make_gcal_event(refined_task):
	"""
	TODO: given all event metadata turn it into a google calendar event
	"""

class AsanaCalendarTask:
	eventData = {	'GCAL_START_TIME_HOUR':0,
					'GCAL_START_TIME_MIN':0,
					'GCAL_END_TIME_HOUR':0,
					'GCAL_END_TIME_MIN':0, 
					'GCAL_AM_OR_PM':0, 
					'EVENT_DESC':''}

	def getData():
		return eventData

	def resetData():
		for x in eventData:
			if x != 'EVENT_DESC':
				x = 0
			else:
				x = ''


		
def main():

	# workspace ID : 15793206719 // 'Asana, Inc'
	# project ID: 215978128317963 // 
	# task ID: 215978128317964

	project_id = '215978128317963'
	client = validate_asana_session()

	task_ids = get_tasks_from_proj(client,project_id)	
	get_task_data(client, task_ids)

		 
	 
if __name__ == '__main__':
	main()