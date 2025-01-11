# task16/views.py
from django.shortcuts import render

def page1(request):
    return render(request, 'task16/page1.html')

def page2(request):
    return render(request, 'task16/page2.html')
