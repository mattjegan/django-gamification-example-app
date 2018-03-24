from django.db import models
from django_gamification.models import GamificationInterface


class ExampleUser(models.Model):
    interface = models.ForeignKey(GamificationInterface, on_delete=models.CASCADE)
