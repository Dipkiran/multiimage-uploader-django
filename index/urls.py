from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^form/$', views.Form, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<id>\d+)/$', views.postdetail, name='detail'),

]
