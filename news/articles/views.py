from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy, reverse

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articles/article_edit.html'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body', 'author')
    success_url = reverse_lazy('article_list')