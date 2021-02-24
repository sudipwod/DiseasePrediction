from django.shortcuts import render, get_object_or_404
from .models import Remedy, Category, Fitness
# Create your views here.


def prevention(request):
    preventions  = Remedy.objects.all()
    return render(request, 'remedieshtml/prevention.html', {'preventions':preventions})


def detail(request, name):
    detail = get_object_or_404(Remedy, slug= name)

    return render(request,'remedieshtml/detail.html',{'detail': detail})


def fitness_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    fitness = Fitness.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        fitness = fitness.filter(category=category)
    return render(request,
                    'remedieshtml/fitness.html',
                    {'category': category,
                    'categories': categories,
                    'fitness': fitness})

    