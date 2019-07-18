from django.urls import path
from . import views

urlpatterns = [
    path('', views.datajson, name='raspi-json'),
    ]
