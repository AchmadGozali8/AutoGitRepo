import sys
import requests
import os

TOKEN = os.environ.get("GIT_TOKEN", None)

def repo_name():
	try:
		return sys.argv[1]
	except IndexError:
		return False

def main_endpoint():
	endpoint = "https://api.github.com"	
	return endpoint

def create_repo():
	endpoint = "/user/repos"
	headers = {"content-type": "application/json", "Authorization": "token {TOKEN}".format(TOKEN=TOKEN)}
	req_url = "{main}{endpoint}".format(main=main_endpoint(), endpoint=endpoint)

	repository_name = repo_name()

	if not repository_name:
		err = {"Error": "Repository name not define"}
		print err
		return err

	data = {"name": repository_name}
	
	response = requests.post(req_url, json=data, headers=headers)

	if not response.ok:
		error = {"error": response.text}
		print error
		print response.url
		print response.headers
		return error

	print "{name} has been created".format(name=repository_name)
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

main()