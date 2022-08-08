from django.urls import re_path
from . import views
#the $ sign besides home restrict the path from having home plus characters and still hit the home path
urlpatterns = [
#  re_path(r'^edit_err/(?P<id>[0-9]+)/$', views.edit_err, name="edit_err"),
#  re_path('edit/<int:id>', views.edit, name="edit"),
 re_path(r'^index$', views.index, name='index'),
#  re_path(r'^add_err$', views.add_err, name="add_err"),
 ]