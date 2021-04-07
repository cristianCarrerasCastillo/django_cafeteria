from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.home, name='services/'),
]