from django.shortcuts import render

from article.models import Article


def index(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset,
    }
    return render(request, 'article/index.html', context=context)


def create(request):
    # GET
    if request.method == 'GET':
        return render(request, 'article/create.html', context={})

    # POST
    return render(request, 'article/create.html', context={})
