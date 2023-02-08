from django.db import models

# Create your models here.

class Venue(models.Model):
    title = models.TextField()
    imgs = models.ImageField(upload_to='venues_pics', blank=True)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    lat = models.DecimalField(max_digits=17, decimal_places=14)