from django.shortcuts import render
from django.views.generic.base import View

from .models import Book


class BooksView(View):
    """Список книг"""

    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html", {'books': books})


class BookDetailView(View):
    """Описание книги"""

    def get(self, request, slug):
        book = Book.objects.get(url=slug)  # url - название поля SlugField в models.py
        return render(request, "books/book_detail.html", {'book': book})

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
