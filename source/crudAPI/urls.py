from django.urls import path
from crudAPI.views.article import ArticleDetailView, ArticleListView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
