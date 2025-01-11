# task17/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dynamic_template, name='dynamic_template'),
]
