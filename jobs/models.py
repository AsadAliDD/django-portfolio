from django.db import models

# Create your models here.
class Job(models.Model):
    title= models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    core_technology = models.CharField(max_length=100,default='')