from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Book, Author


class BooksView(ListView):
    """Список книг"""
    model = Book
    queryset = Book.objects.filter(draft=False)
    template_name = "books/head_page.html"


class AboutBookView(DetailView):
    """Описание книги"""
    model = Book
    slug_field = 'url'  # url - название поля SlugField в models.py
    template_name = "books/about_book.html"


class BookExcerptView(DetailView):
    """Отрывок из книги"""
    model = Book
    slug_field = 'url'
    template_name = "books/book_read_excerpt.html"

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
