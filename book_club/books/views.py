from django.shortcuts import render
from django.views.generic.base import View

from .models import Book


class BooksView(View):
    """Список книг"""

    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html", {'books': books})

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
