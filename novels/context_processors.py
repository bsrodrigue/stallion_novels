from .models import Category

def categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories': all_categories
    }
    return context