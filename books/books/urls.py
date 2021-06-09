from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView


app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='detail'),
    path('search/', SearchResultsListView.as_view(), name='search')
]
