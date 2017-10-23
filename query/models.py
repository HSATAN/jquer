# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=64,default='title')
    content = models.TextField(null=True)

    def __str__(self):
        #这个函数的作用是改变在django后台管理中显示的字符串
        return self.title