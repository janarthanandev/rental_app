from django.conf.urls import url
from . import views
app_name = "rental_app"
urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^rented/(?P<id>[0-9]+)/$', views.rented, name='rented'),
]