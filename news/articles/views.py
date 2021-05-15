from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.urls import reverse_lazy, reverse

from .models import Article



class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class LoginRequired(LoginRequiredMixin):
    login_url = 'login'


class UserAuthorized(UserPassesTestMixin):

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArticleCreateView(LoginRequired, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    # fields = ('title', 'body', 'author')
    fields = ('title', 'body')
    # default success_url is detail view (somehow)
    # success_url = reverse_lazy('article_list')

    # Set author form field to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(LoginRequired, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequired, UserAuthorized, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articles/article_edit.html'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(LoginRequired, UserAuthorized, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
