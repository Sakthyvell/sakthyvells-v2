from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Article


class BlogListingView(ListView):
    template_name = 'blog-listing.html'
    model = Article
    context_object_name = 'posts'
    paginate_by=10

class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog-detail.html'


class BlogCategoryListView(ListView):
    template_name = 'blog-listing.html'
    model = Article


def CategoryListView(request, pk):
    category_posts = Article.objects.filter(category = pk)
    return render(request, 'blog-categories.html', {'posts' : category_posts})
