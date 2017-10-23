from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index$',views.index),
    url(r'^article/(?P<page_id>\d+)',views.article_page,name='article'),
    url(r'^add_article',views.add_artilce,name='add_article'),
    url(r'edit_article/(?P<page_id>\d+)',views.edit_article,name='edit_article'),
    url(r'userinfo/',views.userinfo,name='userinfo'),
    url(r'douban',views.get_douban_top250,name='douban'),
    url(r'userinfo_post$',views.userinfo_post,name='userinfo_post'),
    url(r'auth$',views.auth)
]