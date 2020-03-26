from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.
class Counter(models.Model):
    total_hospital= models.IntegerField()

    today_confirmed = models.IntegerField()
    total_confirmed = models.IntegerField()

    today_recovered = models.IntegerField()
    total_recovered = models.IntegerField()

    today_death = models.IntegerField()
    total_death = models.IntegerField()

    total_isolation = models.IntegerField(null=True)
    Exempt_isolation = models.IntegerField(null=True)
    present_isolation = models.IntegerField(null=True)

    total_quarantine = models.IntegerField(null=True)
    Exempt_quarantine = models.IntegerField(null=True)
    present_quarantine = models.IntegerField(null=True)

    lockdown = models.IntegerField(null=True)



class Myth(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(default='myth_pics/default.jpg', upload_to='myth_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
