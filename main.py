import sys
import requests
import os
import getopt
import argparse

TOKEN = os.environ.get("GIT_TOKEN", None)
# TO-DO
# [ ] Add lists gitignore template

def argument_option():
	data = {}

	parser = argparse.ArgumentParser(description="Automate to create repository on github by @achmad.gz", usage='%(prog)s -n <Repository Name> [-g <Gitignore Template ex: Python>] [-p <Set Repository as Private>]')
	parser.add_argument("-n", "--name", required=True,metavar='', help="Repository name")
	parser.add_argument("-p", "--private", default=False,  action='store_true',help="Set repository as private")
	parser.add_argument("-g", "--gitignore",metavar='', help="Add gitignore template")
	args = parser.parse_args()

	if args.gitignore:
		data['gitignore_template'] = args.gitignore

	data['private'] = args.private
	data['name'] = args.name

	return data

def main_endpoint():
	endpoint = "https://api.github.com"	
	return endpoint

def create_repo():
	endpoint = "/user/repos"
	headers = {"content-type": "application/json", "Authorization": "token {TOKEN}".format(TOKEN=TOKEN)}
	req_url = "{main}{endpoint}".format(main=main_endpoint(), endpoint=endpoint)

	parameters = argument_option()

	response = requests.post(req_url, json=parameters, headers=headers)

	if not response.ok:
		error = {"error": response.text}
		print error
		return error

	print "{name} has been created".format(name=parameters["name"])
	return response.json()

def clone_repo(url):
	command = "git clone {url}".format(url=url)
	os.system(command)

def main():

	if TOKEN is None:
		error = {"Error": "Token is empty"}
		print error
		return error

	response = create_repo()

	ssh_url = response.get("ssh_url", None)
	
	clone_repo(ssh_url)

if __name__ == "__main__":
	main()