from django.contrib import admin
from .models import  PersonManager,Person,PlaceStatus,Place
# Register your models here.

admin.site.register(Person)
admin.site.register(PlaceStatus)
admin.site.register(Place)
