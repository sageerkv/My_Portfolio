from django.db import models

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
    about_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    
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