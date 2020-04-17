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


class Coronacounter(models.Model):
    today_confirmed = models.IntegerField()
    total_confirmed = models.IntegerField()

    today_recovered = models.IntegerField()
    total_recovered = models.IntegerField()

    today_death = models.IntegerField()
    total_death = models.IntegerField()

    total_quarantine = models.IntegerField(null=True,blank=True)
    released_quarantine = models.IntegerField(null=True,blank=True)
    present_quarantine = models.IntegerField(null=True,blank=True)

    total_isolation = models.IntegerField(null=True,blank=True)
    released_isolation = models.IntegerField(null=True,blank=True)
    present_isolation = models.IntegerField(null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_posted.strftime("%d-%m-%Y"))






class Division(models.Model):
    division = models.CharField(max_length=32)

    def __unicode__(self):
        return self.division
    def __str__(self):
        return self.division


class Area(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.CharField(max_length=220,default="Dhaka")
    location = models.CharField(max_length=220,unique=True,null=True,blank=True)
    confirmed_cases = models.IntegerField() 
    up_case = models.IntegerField(blank=True,default=0)
    last_update = models.DateTimeField(default=timezone.now,null=True,blank=True)


    class Meta:
        ordering = ['division','-confirmed_cases']
     

    def __unicode__(self):
        return self.name

    def __str__(self):
        return '{}-{}-{}'.format(self.location,self.district,self.division)
