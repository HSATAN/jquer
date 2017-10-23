# _*_ coding:utf-8 _*_
from django.conf.urls import url
from query.views import index
urlpatterns = [
    url(r'^$',index),
    url(r'^index/$',index)
]