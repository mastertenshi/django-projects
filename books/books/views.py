from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'books/list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'books_list'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            query = query.split(' ')
            search_books = Q()

            for q in query:
                search_books |= Q(title__icontains=q)
                search_books |= Q(author__icontains=q)

            return Book.objects.filter(search_books)
