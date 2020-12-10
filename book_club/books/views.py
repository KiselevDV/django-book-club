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
        # Django заполнит форму ReviewForm данными из request.POST
        form = ReviewForm(request.POST)
        # получение записи из бд по id - объект book
        book = Book.objects.get(id=pk)
        # Проверяем форму на валидность - если да сохраняем
        if form.is_valid():
            # указываем к какому объекту привязывем отзыв
            # приостанавливаем сохранение формы для внесения изменений
            form = form.save(commit=False)
            # ищем в POST запросе ключ parent - имя поля в HTML
            # <input type="hidden" name="parent" id="contactparent" value="">
            if request.POST.get("parent", None):
                # полю parent_id (_id - добавляем число а не объект) достаём значение ключа
                # преобразрвав из строки в int
                form.parent_id = int(request.POST.get("parent"))
            # form.book_id = pk  # указывем объект к которому нужно привязаться
            # присваиваем полю book форме form объект book
            form.book = book
            # данные из формы будут записанны в базу
            form.save()
        return redirect(book.get_absolute_url())

# Логика приложения (принимает запросы и возращает ответы)
# Create your views here.
