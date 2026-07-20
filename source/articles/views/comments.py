from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView

from articles.forms import CommentForm
from articles.models import Article, Comment


class CommentCreateView(CreateView):
    template_name = "comments/comment_create.html"
    form_class = CommentForm
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        artice = get_object_or_404(Article, pk=self.kwargs["pk"])
        form.instance.article = artice
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentLikes(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment_id = self.kwargs.get('comment_pk')
        comment= Comment.objects.get(pk=comment_id)
        user = self.request.user
        if user.is_authenticated:
            if comment.likes.filter(id=user.id).exists():
                comment.likes.remove(user)
                like = "unlike"
            else:
                comment.likes.add(user)
                like = "like"
            return JsonResponse({
                "like": like,
                "count": comment.likes.count()
            })
