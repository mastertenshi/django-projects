from django.urls import path

from .views import BlogDetailView, BlogListView


# Adds scope for when using URL
# ex. {% url 'blog:home' %}
#     {% url 'blog:post_detail' %}
app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
