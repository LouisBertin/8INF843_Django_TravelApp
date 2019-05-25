from django.db import models

# Create your models here.
class Post(models.Model):
    departure = models.CharField(max_length=255)
    arrival = models.CharField(max_length=255)
    passengers_nb = models.IntegerField()
    full = models.BooleanField()
    pub_date = models.DateTimeField('date published')