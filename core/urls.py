from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('sample/', views.sample, name='sample'),
]
