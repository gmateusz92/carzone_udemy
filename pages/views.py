from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True) #featrued cars na stronie
    all_cars = Car.objects.order_by('-created_date') #latest cars na stronie
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

def contact(request): #jezeli chcemy przechowywac dane w azie danych tworzymy model, jezeli nie to bedzie zwykly email
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding' + subject
        message_body = 'Name:' + name + '. Email:' + email + ' . Phone:' + phone + '. Message:' + message

        admin_info = User.objects.get(is_superuser=True)  # wchcemy zeby wyslac email na superusera-admina
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'gmateusz92@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')


