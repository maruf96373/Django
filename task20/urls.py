# task20/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_example, name='static_example'),
]
