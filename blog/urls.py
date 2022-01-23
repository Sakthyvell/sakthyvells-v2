from django.urls import path
from .views import BlogListingView, BlogDetailView


urlpatterns = [
    path('', BlogListingView.as_view(), name='blog-listing'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
