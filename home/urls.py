from django.urls import path

from . import views
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('index', HomeListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("events/", views.eventList, name="events"),
    path("events/<slug:slug>", EventDetailView.as_view(), name="events-details"),
    path("blogs/", blogList.as_view(), name="blogs"),
    path("blogs/<slug:slug>", BlogDetailView.as_view(), name="blog-details"),
]
