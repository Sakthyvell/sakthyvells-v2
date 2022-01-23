from django.views.generic import TemplateView
from .models import Project, Work, School

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['works'] = Work.objects.all()
        context['schools'] = School.objects.all()
        return context