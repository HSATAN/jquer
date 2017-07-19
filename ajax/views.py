from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    articles_node=models.Article.objects.exclude(pk=10)
    articles=[]
    for article in articles_node:
        articles.append(article)
    return render(request,'ajax/index.html',{'articles':articles})