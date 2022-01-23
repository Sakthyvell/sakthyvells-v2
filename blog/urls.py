from django.urls import path
from .views import BlogListingView


urlpatterns = [
    path('', BlogListingView.as_view(), name='blog-listing'),
]
