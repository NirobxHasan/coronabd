from django.contrib import admin

from services.models import  Counter,Myth,Coronacounter,Area,Division

admin.site.register(Myth)
admin.site.register(Coronacounter)
admin.site.register(Area)
admin.site.register(Division)
