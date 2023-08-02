from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class My_portfolio(models.Model):
    # home
    home_description = models.TextField()
    fb_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    insta_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    lnkdn_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    gtb_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    twtr_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    resume = models.FileField(upload_to='uploads/', max_length=100)
    home_img = models.ImageField(upload_to='uploads/', max_length=100)

    # about
    about_img = models.ImageField(upload_to='uploads/', max_length=100)
    about_head = models.TextField()
    about_description = models.TextField()
    
    def __str__(self):
        return self.home_description

class Project(models.Model):

    #portfolio
    porject_img = models.ImageField(upload_to='uploads/', max_length=100)
    porject_head = models.TextField()
    porject_description = models.TextField()
    porject_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.porject_head

class Service(models.Model):
    ICON_CHOICES = (
        ('bx bx-code-alt', 'Web Development'),
        ('bx bxs-paint', 'Graphic Design'),
        ('bx bx-code-block', 'Power apps')  # Fix the icon name here
    )
    service_icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    service_title = models.CharField(max_length=100)
    service_description = models.TextField()
    service_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.service_title
    

class Date(models.Model):
    start_date = models.DateField()
    present_or_end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    @property
    def date_range(self):
        if self.is_current:
            return f"{self.start_date.strftime('%b %Y')} - Present · {self._calculate_duration()} mos"
        elif self.present_or_end_date:
            start_month = self.start_date.strftime("%b %Y")
            end_month = self.present_or_end_date.strftime("%b %Y")
            duration = self._calculate_duration()
            return f"{start_month} - {end_month} · {duration} mos"

    def _calculate_duration(self):
        if self.is_current:
            current_date = timezone.now().replace(day=1)
            start = self.start_date.year * 12 + self.start_date.month
            end = current_date.year * 12 + current_date.month
            months = end - start
            return months
        else:
            start = self.start_date.year * 12 + self.start_date.month
            end = self.present_or_end_date.year * 12 + self.present_or_end_date.month
            months = end - start
            return months

    def save(self, *args, **kwargs):
        if self.is_current:
            self.present_or_end_date = None
        elif not self.present_or_end_date:
            current_month = timezone.now().replace(day=1)
            self.present_or_end_date = current_month
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_current:
            return f"{self.start_date.strftime('%B %Y')} - Present · {self._calculate_duration()} mos"
        formatted_date = self.present_or_end_date.strftime("%B %Y") if self.present_or_end_date else "Present"
        return formatted_date

class Experience(models.Model):
    date = models.OneToOneField(Date, on_delete=models.CASCADE, related_name='experience')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')
    
    def __str__(self):
        return self.name
