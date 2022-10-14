from http import client
from django.shortcuts import render
import datetime
from .models import Venue, Customer, Event


def customer(request):
    customer = Customer.objects.all()
    return render(request, "events/customer.html", {
        "customer": customer,
    })


def home(request):
    name = "PreRental"
    now = datetime.datetime.now()
    current_time = now.strftime("%A, %d %B, %Y at %X")
    return render(request, "events/home.html", {
        "current_time": current_time,
    })

def homeCliente(request, name):
    name = "PreRental"
    now = datetime.datetime.now()
    current_time = now.strftime("%A, %d %B, %Y at %X")
    return render(request, "events/home.html", {
        "name": name,
        "current_time": current_time,
    })
