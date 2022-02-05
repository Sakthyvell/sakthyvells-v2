from .models import Category

def categoryList(request):
    category = Category.objects.all()
    return {
        'categories' : category
    }