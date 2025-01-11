# task15/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('view_one/', views.view_one, name='view_one'),
    path('view_two/', views.view_two, name='view_two'),
]
