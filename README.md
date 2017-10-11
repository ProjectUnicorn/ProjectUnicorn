#ProjectUnicorn

Checkout from github



##On Windows bash.exe
```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo apt-get install git
sudo python get-pip.py

git clone https://github.com/ProjectUnicorn/ProjectUnicorn
cd ProjectUnicorn

## Setup virtualenv
Should be next to manage.py

`virtualenv -p python3 projectunicorn-env`
`source projectunicorn-env/bin/activate`

`pip install django`
`pip install django-tables2`
`pip install django-filter`
`pip install djangorestframework`
`pip install markdown`
`pip install mysqlclient`
If mysqlclient install fails, then install the following package, and try again.
`sudo apt-get install libmysqlclient-dev`

## Setup settings
1. Open projectunicorn/settings.py
2. Find ALLOWED_HOSTS and uncomment localhost
3. Find DATABASES and comment/uncomment to fit your database setup


## Setup database
`python manage.py makemigrations`
`python manage.py migrate`

## Start server
`python manage.py runserver 8080`

# API
using HTTPie
	/api/applicationlist
		applicationlist API
		`http get localhost:8000/api/applicationlist/ 'Authorization: Token foo'`
	/api/token
		get token on user.
		`http get localhost:8000/api/token/ username='foo' password='bar'`
