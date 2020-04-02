from django.db import models

# Create your models here.
class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    objects = PersonManager()

    class Meta:
        unique_together = [['first_name', 'last_name']]





class PlaceStatus(models.Model):
    status = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Place statuses"

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.status


class Place(models.Model):
    name = models.CharField(max_length=200)
    coord_v = models.FloatField()
    coord_h = models.FloatField()
    status = models.ForeignKey(PlaceStatus, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
