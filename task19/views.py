# task19/views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    search_query = request.GET.get('q', '')  # Get the search query from the request
    books = Book.objects.all()

    # Apply filtering if a search query is provided
    if search_query:
        books = books.filter(title__icontains=search_query).order_by('title')

    return render(request, 'task19/book_list.html', {'books': books, 'search_query': search_query})
