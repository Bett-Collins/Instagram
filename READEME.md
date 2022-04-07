Instagram
Author
kiprotich Collins
Description
This is an instagram clone that allows user to post their pictures.
Setup and Installation
To get the project .......
Cloning the repository:
https://https://github.com/Bett-Collins/instagram.git
Navigate into the folder and install requirements
cd insta pip install -r requirements.txt
Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate
Install Dependencies
pip install -r requirements.txt
Setup Database
SetUp your database User,Password, Host then make migrate
python manage.py makemigrations instagram
Now Migrate
python manage.py migrate
Run the application
python manage.py runserver
Running the application
python manage.py server
Testing the application
python manage.py test
Open the application on your browser 127.0.0.1:8000.
Technology used
Python3.8
Django 2.0
Heroku
Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

Technology used
Python3.8
[Django]
Heroku
License
MIT License: licence
