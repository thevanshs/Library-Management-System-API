# admin.py

from django.contrib import admin
from .models import Genre, Author, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'city', 'author_id']
    search_fields = ['name', 'email']
    readonly_fields = ['author_id']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'author', 'num_pages']
    search_fields = ['name', 'author__name', 'genre__name']
