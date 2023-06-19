from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import My_portfolio, Project
# from .forms import BookingForm
from django.contrib import messages
from  . import models

# Create your views here.

def index(request):
    myport = models.My_portfolio.objects.all()
    project  = models.Project.objects.all()
    return render(request,"index.html",{'myport':myport,'project':project})

