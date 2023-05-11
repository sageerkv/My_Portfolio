from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import My_portfolio
# from .forms import BookingForm
from django.contrib import messages

# Create your views here.

def index(request):
    dict_myport = {
        'myport':My_portfolio.objects.all()
    }
    # dict_Project = {
    #     'Project':project.objects.all()
    # }
    # context ={'dict_myport':dict_myport,'dict_Project':dict_Project}
    return render(request,"index.html",dict_myport)

