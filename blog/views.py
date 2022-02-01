from pipes import Template
from pyexpat import model
from unicodedata import category
from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
from .models import Article, Category


class BlogListingView(ListView):
    template_name = 'blog-listing.html'
    model = Article
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog-detail.html'


class BlogCategoryListView(ListView):
    template_name = 'blog-listing.html'
    model = Article


def CategoryListView(request, pk):
    category_posts = Article.objects.filter(pk = pk)
    return render(request, 'blog-categories.html', {'posts' : category_posts})
