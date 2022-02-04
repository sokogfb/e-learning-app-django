from django.urls import path

from . import views
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path("contact/", views.contact, name="contact"),
]
