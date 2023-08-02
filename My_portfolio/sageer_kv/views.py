from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import My_portfolio, Project, Service, Experience, Skill
# from .forms import BookingForm
from django.contrib import messages
from  . import models 

from django.core.mail import EmailMessage
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



MAX_ALLOWED_FILE_SIZE_IN_BYTES = 10 * 1024 * 1024  # 10 MB (adjust the value as needed)

def contact_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')  # Get the uploaded file

        # Basic form validation
        if not full_name or not email or not message:
            messages.error(request, "Please fill in all required fields (Full Name, Email, Message).")
            return redirect('index')

        # Check file size
        if attachment:
            file_size_bytes = attachment.size
            if file_size_bytes > MAX_ALLOWED_FILE_SIZE_IN_BYTES:
                max_allowed_size_mb = MAX_ALLOWED_FILE_SIZE_IN_BYTES / (1024 * 1024)
                messages.error(request, f"File size exceeds the allowed limit. Maximum allowed size is {max_allowed_size_mb:.2f} MB.")
                return redirect('index')

        # Compose email message
        email_subject = 'Contact Form Submission'
        email_message = f"Full Name: {full_name}\n"
        email_message += f"Email: {email}\n"
        email_message += f"Mobile Number: {mobile_number}\n"
        email_message += f"Subject: {subject}\n"
        email_message += f"Message: {message}"

        # Create an EmailMessage object
        email = EmailMessage(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
        )

        # Attach the file to the email, if provided
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        # Send the email
        email.send()

        # Add a success message
        messages.success(request, f"Dear {full_name}, Your message has been sent! Thank you.")
        return redirect('index')

    # If the request method is GET or the form submission fails, render the index page
    myport = My_portfolio.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', {'myport': myport, 'project': project})







