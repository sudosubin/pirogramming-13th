from django.urls import path, include, reverse

from article.views import (index, create, retrieve,
                           update, delete)

app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('create/', create, name='create'),
    path('article/<int:pk>/', retrieve, name='retrieve'),
    path('article/<int:pk>/update/', update, name='update'),
    path('article/<int:pk>/delete/', delete, name='delete'),
]
