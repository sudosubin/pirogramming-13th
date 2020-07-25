from django.shortcuts import render, redirect

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
    title = request.POST['title']
    content = request.POST['content']
    article = Article.objects.create(title=title, content=content)

    pk = article.id
    return redirect(to='/article/{}/'.format(pk))


def retrieve(request, pk):
    article = Article.objects.get(id=pk)

    context = {
        'article': article
    }

    return render(request, 'article/retrieve.html', context=context)


def update(request, pk):
    article = Article.objects.get(id=pk)

    # GET
    if request.method == 'GET':
        context = {
            'article': article
        }
        return render(request, 'article/update.html', context=context)

    return render(request, 'article/update.html', context={})
