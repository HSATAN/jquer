from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    articles=models.Article.objects.exclude(pk=10)
    return render(request,'ajax/index.html',{'articles':articles})