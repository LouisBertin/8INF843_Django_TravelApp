from django.db import models

# Create your models here.
class Post(models.Model):
    departure = models.CharField(max_length=255)
    arrival = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    passengers_nb = models.IntegerField()
    full = models.BooleanField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title