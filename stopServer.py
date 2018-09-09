#! /usr/bin/env python3
# encoding: utf-8

#
#		Script to stop a running EC2 instance. Lot's of cut and paste from the start script.
#
#   The Python3 version (just changed the print statements)

#		Sid Stuart
#		Sept 2, 2018
#

import boto3
import argparse
import sys
import time

# Pick up the AWS profile to use and the name of the instance to start.
PARSER = argparse.ArgumentParser("Start an EC2 instance in jeanco, if it is not running")
PARSER.add_argument('--profile', '-p', default='jeanco', help='The name of the AWS profile to use.')
PARSER.add_argument('--name', '-n', default='jeanServer', help='The name of the instance to start')
PARSER.add_argument('--region', '-r', default='us-west-1', help='Set the region to investigate, default is N. California')
ARGS = PARSER.parse_args()

def main():
	''' Set up the AWS credentials and then call a function check the status
	    of the instance. If it is down, start it. If it is up do nothing. In either
	    case, return the IP address of the instance.
	'''
	try:
		session = boto3.session.Session(profile_name=ARGS.profile, region_name=ARGS.region)
		(is_running, ip, state, instance_id, count) = instance_running(session, ARGS.name)
		print (f'There are {count:d} instance(s) running')
		if is_running:
			print ('Stopping server')
			result = stop_server(session, ARGS.region, instance_id, ARGS.name)
			print (f'Stopped Minecraft server {ARGS.name}')
		else:
			print (f'Server {ARGS.name} is not running')

	# The boto documentation does a poor job of documenting what exceptions are thrown,
	# so use a catch all and hope for the best.
	except:
		(except_type, value) = (sys.exc_info()[:2])
		print (f'Unexpected error in main, type {except_type}, value {value}')
		sys.exit(-1)


def instance_running(session, name):
	''' Grab a ec2 client class and look for an instance with the provided name.
	    If it is found and has the state running, the set the is_running flag and
	    grab the IP address to return as well. Along the way, keep a count
	    of all the instance that are running and return that as well.
	'''
	try:
		client = session.client('ec2', ARGS.region)
		instances = client.describe_instances()
		# For some reason, the reservations is stored in a list inside the dict. 
		# So index the dict and then pop off the first item on the list. 
		reservations = instances['Reservations'].pop(0)
		instance_list = reservations['Instances']
		count = 0
		is_running = False
		for instance in instance_list:
			if instance['State']['Name'] == 'running':
				count = count + 1
				if instance['KeyName'] == ARGS.name:
					is_running = True
		if is_running == True:
			return (is_running, instance['PublicIpAddress'], instance['State']['Name'], instance['InstanceId'], count)
		else:
			return (is_running, None, None, instance['InstanceId'], count)
	except:
		(except_type, value) = (sys.exc_info()[:2])
		print (f'Unexpected error in isntance_running, type {except_type}, value {value}')
		sys.exit(-1)


def stop_server(session, region, instance_id, name):
	''' Stop a running server. The code has already check to see if the server is running.
			So just get a resource and stop it.
	'''
	ec2 = session.resource('ec2', region)
	instance = ec2.Instance(instance_id)
	response = instance.stop()
	# Wait a bit for it to shut down
	time.sleep(20)
	(is_running, ip, state, instance_id, count) = instance_running(session, name)
	if is_running:
		print ('It is still running, waiting for a minute')
		time.sleep(60)
		(is_running, ip, state, instance_id, count) = instance_running(session, name)
		if is_running:
			print ('Argh! {name} is still running, shut it down through the console.')



if __name__ == '__main__':
	main()