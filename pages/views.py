from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True) #featrued cars na stronie
    all_cars = Car.objects.order_by('-created_date') #latest cars na stronie
    return render(request, 'pages/home.html', {'teams': teams, 'featured_cars': featured_cars, 'all_cars': all_cars})

def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html', {'teams': teams})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
