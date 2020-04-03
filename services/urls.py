from django.conf.urls import url
from django.urls import path
from . import views
from services.views import CoronaChartView

urlpatterns = [
    path('myths/',views.myths, name='myths'),
     path('',CoronaChartView.as_view(), name='chart')

]
