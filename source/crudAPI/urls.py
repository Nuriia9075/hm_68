from django.urls import path
from crudAPI.views.article import ArticleDetailView, ArticleListView
from crudAPI.views.comment import CommentListCreateView, CommentDetailUpdateDeleteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:article_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailUpdateDeleteView.as_view(), name='comment-detail-update-delete'),
]
