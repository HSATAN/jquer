from django.shortcuts import render
from . import models
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
        print(title)
        print(content)
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
