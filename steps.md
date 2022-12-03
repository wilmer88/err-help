# cheat-snip
* `python --version` checks to see if you have python
* to make a new django env `python -m virtualenv choiceofname`
* for python to offically recognize your virtualenv run `python -m virtualenv --version`
* to activate existing enviorment on command Promt run `.\env\Scripts\activate ` or git bash run ` source your_env/Scripts/activate`
* to install django run `python -m pip install Django`
* to create new django app with env initiated `django-admin startproject urNamechoice` after creating app cd inside directory.
* after you cd inside the newly created app dir next run `python manage.py startapp YourAppName` will create a sibeling app 

* to run python program enter inside app directory `python manage.py runserver`
* To exit your virtualenv sandbox and return to your normal system environmentuse `deactivate`
* To install django run in the same dir you created virtualenv run `python -m pip install Django`

* next go to your created app next go to setttings.py and add `users.apps.UsersConfig` inside the  INSTALLED_APPS =[] array.
 `INSTALLED_APPS =[ 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig']`

* inside users/views.py, if compared to javascript your django controllers will go here.
import `from django.http import HttpResponse` and also
Add `def home(request): response = "<h1>"django is working if your reading this" return HttpResponse(response)` 
inside users/views.py

* Next create `urls.py` file inside users folder. It is crucially important for the file to be named exactly like this.

* next inside the users/urls.py, inside your newlly created `urls.py` file import dependencies
`from django.urls import re_path, include`
`from . import views` 
`urlpatterns = [re_path(r'^home', views.home, name='home')] `
also very crucial to have exact naming for the app to work.

* next, inside app/urls.py import dependencies and add paths from users.urls
`from django.urls import re_path, include`  
inside urlpatterns[] add ` path(r'', include('users.urls')) ` like this
  ` urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('snips.urls')),
]`

* to run python program enter inside app directory in bash or command prompt `python manage.py runserver`
* your app should be running on `localhost:8080/home`
* Create templates to sparate your html/pages from your "controller"/users/views.py and makeyour views dynamic inside of the users folder create a new folder that must called `templates` for django to find. 
* inside of templates creat new folder and name it `users` or what ever you want not sure of the consequences.
* inside of users/templates/users create layout.html file
* inside of layout.html file inside the head tags delete what is inside the title tags and insert like example
`<title>{% block title %}{% endblock %}</title>`

* inside of layout.html file inside the body tags delete what is inside the body tags and insert like example
this will be like {{{ body }}} of main.handlebars file when using handlebars.js
`<body>
{% block content %}
{% endblock %}
</body> `

* create another html file called index.html file and inside this file type
 `{% extends 'users/layout.html %} `
 `{% block title %} Welcome to Index {% endblock %} `
 ` {% block content %}   `
  ` <h1>congrats with django if reading this</h1>`
  `{% endblock %}`

# data_base-notes
* run `python manage.py shell` after creating models to load app to memory by runing powershell with python
* run ` from users.models import User`
* import User from snips/modeles by runing ` from snips.models import Snipit `

* on gitbash or command prompt run ` python manage.py makemigrations` creates orm makes migration
* on gitbash or command prompt run ` python manage.py migrate ` runs migration
* inside of `python manage.py shell` create snip/user with a variable like this `userrr = User(first_name="will", email="@yahoo.com", etc)`
* save user by runing ` userrr.save() `
* `User.objects.all()` gets whole collection/table data

# python-notes
- using django is like having and using express and handlebars together. 
- python has very strict indentation
- python dictionary looks like javascript object but is not an object
- best way to iderate thru a dictionary
`student_profile = {
        'first_name' : 'Jane',
        'last_name' : 'Doe',
        'middle_initial' : 'Q',
        'address' : 'Melbourne, Australia',
        'email' : 'jane@gmail.com',
        'phone_number' : '5555555678' ,
        }
for key, value in student_profile.items():
    print('The key {0} has value {1}.'.format(key, value))`

## array examples
`arr = [1,2,3,4]`
-iderate backwards `arr[::-1]`

-every other index backwards `arr[::-2]`

-standerd iderate `arr[::1]`

-iderate every other index `arr[::2]`

- to append `arr.append(5)` will append 5 to `arr= [1,2,3,4]`

-adds contents of one array to another array `arr +=[6,7]`or `arr.extends([6,7])`
`print(arr)` will print [1,2,3,4,5,6,7])

-