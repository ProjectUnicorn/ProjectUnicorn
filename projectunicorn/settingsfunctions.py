import os
def check_if_sql_directory_exists(path):
	path = path.split('/')
	del path[-1]
	del path[-1]
	pathToCheck = ""
	for i in range(0, len(path)):
		pathToCheck += path[i] + "/"
		if(i == len(path)-1):
			pathToCheck += "MySQL-Credentials.cnf"
	if os.path.exists(pathToCheck):
		return True
	else:
		return False

