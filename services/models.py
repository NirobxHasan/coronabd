from django.db import models

# Create your models here.
class Counter(models.Model):
    total_hospital= models.IntegerField()

    today_confirmed = models.IntegerField()
    total_confirmed = models.IntegerField()

    today_recovered = models.IntegerField()
    total_recovered = models.IntegerField()

    today_death = models.IntegerField()
    total_death = models.IntegerField()
