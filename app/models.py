from django.db import models
from django.contrib.auth.models import AbstractUser


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


class User(AbstractUser):
    money = models.IntegerField(default=300)

    def __str__(self):
        return self.email

class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cigarette = models.BooleanField()
    animal = models.BooleanField()
    discussion = models.BooleanField()
    big_suitcase = models.BooleanField()

    def __str__(self):
        return self.user
