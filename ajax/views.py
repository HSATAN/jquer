# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
import requests
# Create your views here.
def index(request):
    articles=models.Article.objects.all()
    return render(request,'ajax/index.html',{'articles':articles})
def article_page(request,page_id):
    article=models.Article.objects.get(pk=page_id)
    return render(request,'ajax/article.html',{'article':article})
def add_artilce(request):
    if request.method=="GET":
        return render(request,'ajax/add_article.html')
    else:
        title=request.POST.get('title','没有title')
        content=request.POST.get('content','内容为空')
        #也可以使用request.POST['title']
        articles=models.Article.objects.all()
        return render(request,'ajax/index.html',context={'articles':articles})
    pass
def edit_article(request,page_id):
    article=models.Article.objects.get(pk=page_id)
    title=request.POST.get('new_title')
    content=request.POST.get('new_content')
    article.title=title
    article.content=content
    article.save()
    return render(request,'ajax/article.html',{'article':article})
    pass

def userinfo(request):
    return HttpResponse(json.dumps({"name":"黄开杰","age":25,"id":1,"password":"123456"}))

def get_douban_top250(request):

    url = "https://api.douban.com/v2/movie/top250?start=0&count=10"
    response = requests.get(url)
    return HttpResponse(response.content)
def userinfo_post(request):
    id = request.POST.get("id",0)
    if int(id) == 1:
        return HttpResponse(json.dumps({"code":11111,"name": "黄开杰", "age": 25, "id": 1, "password": "123456"}))
    return HttpResponse({"code":20002,"message":"验证失败"})

def auth(request):
    id = request.POST.get("id", "")
    if id == "黄开杰":
        return HttpResponse(json.dumps({"number":999,"code":11111,"name": "黄开杰", "age": 25, "id": 1, "password": "123456"}))
    return HttpResponse(json.dumps({"code": 20002, "message": "验证失败"}))