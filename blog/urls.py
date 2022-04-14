from django.urls import path
from .views import BlogListingView, BlogDetailView, CategoryListView


urlpatterns = [
    path('', BlogListingView.as_view(), name='blog-listing'),
    # path('article/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('article/<int:pk>/', BlogDetailView, name='blog-detail'),
    path('category/<int:pk>/', CategoryListView, name='blog-category'),
]
