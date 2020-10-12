from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Book
from .forms import ReviewForm


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)  # Django заполнит форму ReviewForm данными из request.POST
        book = Book.objects.get(id=pk)  # получение записи из бд по id - объект book
        if form.is_valid():  # Проверяем форму на валидность - если да сохраняем
            # указываем к какому объекту привязывем отзыв
            # приостанавливаем сохранение формы для внесения изменений
            form = form.save(commit=False)
            # form.book_id = pk  # указывем объект к которому нужно привязаться
            form.book = book  # присваиваем полю book форме form объект book
            form.save()  # данные из формы будут записанны в базу
        return redirect(book.get_absolute_url())

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
