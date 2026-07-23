from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models.article import Article
from crudAPI.serializers import ArticleSerializer
from rest_framework import status
from django.contrib.auth import get_user_model

# Create your views here.
class ArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        User = get_user_model()
        test_user = User.objects.first()
        if test_user:
            if serializer.is_valid():
                serializer.save(author=test_user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['pk'])
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['pk'])
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['pk'])
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

