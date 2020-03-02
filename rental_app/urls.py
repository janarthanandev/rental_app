from django.conf.urls import url
from . import views
from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView


app_name = "rental_app"
urlpatterns = [
    url(r'home', views.home, name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^rent/$', views.rent, name='rent'), 
    url(r'^rented/(?P<id>[0-9]+)/$', views.rented, name='rented'),
    path('signup/', SignUpView.as_view(), name='signup'),
]