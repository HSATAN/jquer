from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from ajax.views import index
urlpatterns=[
    url(r'^$',index),
    url(r'^index$',index)
]