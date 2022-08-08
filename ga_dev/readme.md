## heroku deployment commands and steps
`apt-get build-dep python-psycopg2`
`pip install dj-database-url`
`pip install whitenoise`
`deactivate`
`pip install dj-database-url`
`heroku run python manage.py migrate`
`git init  heroku apps heroku git:remote -a your_app_name`