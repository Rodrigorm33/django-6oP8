from django.urls import path
from . import views

app_name = 'multas'

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.buscar, name='buscar'),
] 