from django.views.generic import TemplateView

from books.views import SearchResultsListView


class HomeView(SearchResultsListView):
    template_name = 'pages/home.html'
    pass


class ErrorView(TemplateView):
    template_name = 'pages/error.html'