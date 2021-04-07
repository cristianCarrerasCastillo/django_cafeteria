from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('store/', views.home, name='store'),
    path('sample/', views.home, name='sample'),
]
