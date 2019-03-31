from django.db import models

# Create your models here.
class Blog(models.Model):

    blog_id = models.IntegerField();
    title = models.CharField(max_length=100)
    desciption = models.CharField(max_length=400)