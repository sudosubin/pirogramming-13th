from django.urls import path, include

from article.views import index, create, retrieve, update


urlpatterns = [
    path('', index),
    path('create/', create),
    path('article/<int:pk>/', retrieve),
    path('update/<int:pk>/', update),
]
