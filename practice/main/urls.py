from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing),
    path('home', views.landing),
    path('add-word', views.adding),
    path('word-list', views.wordlist)
]
