from django.shortcuts import render, redirect
from .models import Home
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# My views here.

#home page
def home(request):
    return render(request, 'home.html', {})

def rent(request):
    homes = Home.objects.all()
    return render(request, 'rent.html', {"homes":homes})

def rented(request, id):
    home = Home.objects.get(pk=id)
    print(home.rental_status)
    messages.success(request, "You have rented " + home.name + "!")
    if home.rental_status == 'avail':
        home.rental_status = 'navail'
        messages.success(request, "You have rented " + home.name + "!")
    else:
        messages.success(request, "Home is not available for rent " + home.name + "!")
    home.save()
    return redirect('rental_app:rent')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'