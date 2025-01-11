from django.shortcuts import render

def hello_world(request):
    return render(request, 'task13/hello_world.html')  # Ensure 'task13/' prefix matches your folder structure
