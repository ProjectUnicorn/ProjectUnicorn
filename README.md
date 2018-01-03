# ProjectUnicorn

Application list used for identifying and specifying name, point of contact and responsibilty many systems, services and applications. 

Powered by [Django](https://www.djangoproject.com/)

## Download and prepare
```bash
sudo apt-get install git
sudo apt-get install python3 python3-dev
git clone https://github.com/ProjectUnicorn/ProjectUnicorn
cd ProjectUnicorn
```
Can be done on Windows 10 using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (Install using Powershell and reboot afterwards):

## Setup virtualenv
Should be next to manage.py

```bash
virtualenv -p python3 projectunicorn-env
source projectunicorn-env/bin/activate
pip install -r requirements.txt
```

If mysqlclient install fails, then install the following package, and try again.
```bash
sudo apt-get install libmysqlclient-dev
```
## Setup settings
1. Open projectunicorn/settings.py
2. Find ALLOWED_HOSTS and uncomment localhost
3. Find DATABASES and comment/uncomment to fit your database setup


## Setup database
```bash
python manage.py makemigrations
python manage.py migrate
```

Test data can be loaded:
```bash
python manage.py loaddata testdata.json
```
## Start server
```bash
python manage.py runserver 8080
```

# API
Using [HTTPie](https://httpie.org/):
Get list of all entries: 
```bash
http get localhost:8000/api/applicationlist/ 'Authorization: Token foo'
```
Get single entry where "1" is the application id specified on every application:
```bash
http get localhost:8000/api/application/1
```
Get token:
```bash
http get localhost:8000/api/token/ username='foo' password='bar'
```