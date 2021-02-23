from django.urls import path, include
from . import views

app_name='ventas'

urlpatterns = [
    path('', views.homepage, name='homepage')
]