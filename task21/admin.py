# task21/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define what fields to display in the list view
    list_display = ('title', 'author', 'published_date')
    # Add filters for the admin interface
    list_filter = ('author', 'published_date')
    # Add search functionality
    search_fields = ('title', 'author')

# Register the model with the custom admin options
admin.site.register(Book, BookAdmin)
