# cal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('submitquery/', views.submit_query, name='submit_query'),
    
]
