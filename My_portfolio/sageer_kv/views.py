from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import My_portfolio, Project, Service, Experience, Skill
# from .forms import BookingForm
from django.contrib import messages
from  . import models 

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    myport = models.My_portfolio.objects.all()
    project  = models.Project.objects.all()
    services = models.Service.objects.all()
    experiences = Experience.objects.all()
    skills_list = Skill.objects.all()
    context = {'myport':myport,'project':project,'services': services, 'experiences': experiences, 'skills_list': skills_list}
    return render(request,"index.html", context)

def contact_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Compose email message
        email_message = f"Full Name: {full_name}\n"
        email_message += f"Email: {email}\n"
        email_message += f"Mobile Number: {mobile_number}\n"
        email_message += f"Subject: {subject}\n"
        email_message += f"Message: {message}"

        # Send email
        send_mail(
            'Contact Form Submission',
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Optionally, you can add a success message or redirect to a thank you page
        messages.success(request, f"Dear {full_name}, Your message has been sent! Thank you.")
        return redirect('index')

    # If the request method is GET or the form submission fails, render the index page
    myport = My_portfolio.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', {'myport': myport, 'project': project})


