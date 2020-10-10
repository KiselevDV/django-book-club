from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Book, Author


class BooksView(View):
    """Список книг"""

    def get(self, request):
        books = Book.objects.filter(draft=False)
        authors = Author.objects.all()
        return render(request, "books/books.html", {'books': books, 'authors': authors})


class BookDetailView(View):
    """Описание книги"""

    def get(self, request, slug):
        book = Book.objects.get(url=slug)  # url - название поля SlugField в models.py
        authors = Author.objects.all()
        return render(request, "books/book_detail.html", {'book': book, 'authors': authors})

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
