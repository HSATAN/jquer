# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
import query.models as models
# Create your views here.
def index(request):
    #return HttpResponse('hello world')
    article=models.Article.objects.get(pk=1)
    return render(request,'query/index.html',{'article':article})
