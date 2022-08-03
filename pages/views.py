from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True) #featrued cars na stronie
    all_cars = Car.objects.order_by('-created_date') #latest cars na stronie
    #search_fields = Car.objects.values('model', 'city', 'year', 'body_style') # pobiera wartosci z klacy Car do wyszukiwarki na stronie home
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct() #value list flat=True zwraca liste a nie slownik
    year_search = Car.objects.values_list('year', flat=True).distinct() # distinct() zapobiega pobieraniu takich samych wierszy z bazy danych
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {  'model_search': model_search,
              'city_search': city_search,
              'year_search': year_search,
              'body_style_search': body_style_search,
              'teams': teams,
              'featured_cars': featured_cars,
              'all_cars': all_cars,
              }

    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html', {'teams': teams})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
