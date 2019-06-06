from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cigarette = models.BooleanField(default=False)
    animal = models.BooleanField(default=False)
    discussion = models.BooleanField(default=True)
    big_suitcase = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def create_user_preference(sender, instance, created, **kwargs):
    if created:
        Preference.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_preference(sender, instance, **kwargs):
    instance.preference.save()
