from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/',default='images/default.png')

    def summary(self):
        return self.content[:100]


    def date_format(self):
        return self.date.strftime('%b %e %Y')


    def __str__(self):
        return self.title