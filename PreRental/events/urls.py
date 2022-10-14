from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:name>/', views.homeCliente, name="homeCliente"),
    path('customer', views.customer, name='customer'),
]

