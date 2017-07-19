from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index$',views.index),
    url(r'^article/(?P<page_id>\d+)',views.article_page,name='article'),
    url(r'^add_article',views.add_artilce,name='add_article'),
    url(r'edit_article/(?P<page_id>\d+)',views.edit_article,name='edit_article')
]