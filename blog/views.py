from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Article
from django.contrib.auth.models import User



class BlogListingView(ListView):
    template_name = 'blog-listing.html'
    model = Article
    context_object_name = 'posts'
    paginate_by=10


class BlogCategoryListView(ListView):
    template_name = 'blog-listing.html'
    model = Article


def CategoryListView(request, pk):
    category_posts = Article.objects.filter(category = pk)
    return render(request, 'blog-categories.html', {'posts' : category_posts})

def BlogDetailView(request, pk):
    post = Article.objects.get(pk=pk)
    author = User.objects.filter(username=post.author)
    post.authorName = author[0].first_name+' '+ author[0].last_name
    return render(request, 'blog-detail.html', {'object' : post})