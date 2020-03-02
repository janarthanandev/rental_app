from django.shortcuts import render, redirect
from .models import Home
from django.contrib import messages
# My views here.

#home page
def home(request):
    return render(request, 'home.html', {})

def rent(request):
    home = Home.objects.all()
    return render(request, 'rent.html', {"home":home})

def rented(request, id):
    home = Home.objects.get(pk=id)
    if home.rental_status == 'avail':
        home.rental_status -= 'navail'
        messages.success(request, "You have rented " + home.name + "!")
    else:
        messages.success(request, "Home is not available for rent " + home.name + "!")
    home.save()
    return redirect('django_rental:rent')