from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models.comments import Comment
from articles.models.article import Article
from crudAPI.serializers import CommentSerializer
from rest_framework import status
from django.contrib.auth import get_user_model


# Create your views here.
class CommentListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['article_id'])
        objects = article.comments.all()
        serializer = CommentSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        article = get_object_or_404(Article, pk=kwargs['article_id'])
        User = get_user_model()
        test_user = User.objects.first()
        if test_user:
            if serializer.is_valid():
                serializer.save(author=test_user, article=article)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailUpdateDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs['pk'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs['pk'])
        comment_id = comment.id
        comment.delete()
        return Response({"id": comment_id}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs['pk'])
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

