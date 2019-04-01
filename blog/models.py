from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    desciption = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/',default='images/default.png')