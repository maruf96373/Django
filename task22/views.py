# task22/views.py
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid data to the database
            return redirect('book_list')  # Redirect to a list view (or another page)
    else:
        form = BookForm()
    return render(request, 'task22/add_book.html', {'form': form})
