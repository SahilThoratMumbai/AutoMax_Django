from django.urls import path
from .views import main,domain

urlpatterns = [
    path("",main,name='main'),
    path("domain/",domain,name='domain'),
    
]