from importlib.resources import path
from django.urls import re_path 
# from django.urls import path

from . import views
#the $ sign besides home restrict the path from having home plus characters and still hit the home path
urlpatterns = [
re_path(r'^index$', views.index, name='index'),


 re_path(r'^add$', views.add, name="add"),
  re_path(r'^$', views.index, name='index'),
   re_path(r'edit/<int:id>/', views.edit, name="edit"),
   #  re_path(r'^edit/(?P<id>[0-9]+)/$', views.edit, name="edit"),
 ]