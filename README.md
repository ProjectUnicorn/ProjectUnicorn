#ProjectUnicorn

Checkout from github

run:
virtualenv -p python3 projectunicorn-env

you should now have a projectunicorn-env folder next to manage.py


##On Windows bash.exe

wget https://bootstrap.pypa.io/get-pip.py
sudo apt-get install git
sudo python get-pip.py

git clone https://github.com/ProjectUnicorn/ProjectUnicorn
cd ProjectUnicorn
vim projectunicorn/settings.py # tilføj 127.0.0.1 i ALLOWED_HOSTS og ændr til
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

virtualenv -p python3 projectunicorn-env
source projectunicorn-env/bin/activate

pip install django
pip install django_tables2
pip install django_filter <-- filters? 

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080
