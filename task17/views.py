# task17/views.py
from django.shortcuts import render

def dynamic_template(request):
    # Dynamic data to pass to the template
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    ]
    message = "This is dynamically generated content using context dictionaries."

    # Pass data to the template using a context dictionary
    context = {
        'books': books,
        'message': message,
    }
    return render(request, 'task17/dynamic_template.html', context)
