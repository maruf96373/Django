# task14/views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'task14/book_list.html', {'books': books})
