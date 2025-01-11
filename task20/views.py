# task20/views.py
from django.shortcuts import render

def static_example(request):
    return render(request, 'task20/static_example.html')
