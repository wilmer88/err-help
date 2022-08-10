from django.urls import re_path
from . import views
#the $ sign besides home restrict the path from having home plus characters and still hit the home path
urlpatterns = [
 re_path(r'^edit/(?P<id>[0-9]+)/$', views.edit, name="edit"),
#  re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete"),
 re_path(r'^$', views.index, name='index'),
#  re_path(r'^index$', views.index, name='index'),
 re_path(r'^add$', views.add, name="add")
 ]