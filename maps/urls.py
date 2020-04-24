from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('maps/', views.map, name="map"),
    path('posts/', views.posts, name='posts'),
    
]