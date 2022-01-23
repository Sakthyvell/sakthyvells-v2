from pipes import Template
from pyexpat import model
from django.views.generic import TemplateView, DetailView
from .models import Article, Category


class BlogListingView(TemplateView):
    template_name = 'blog-listing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context

class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog-detail.html'

    