# _*_ coding:utf-8 _*_
from django.contrib import admin
from .models import  Article
# Register your models here.
admin.site.register(Article)#注册model,可以在项目管理中查看