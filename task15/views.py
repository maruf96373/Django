# task15/views.py
from django.http import HttpResponse

def view_one(request):
    return HttpResponse("This is View One!")

def view_two(request):
    return HttpResponse("This is View Two!")
