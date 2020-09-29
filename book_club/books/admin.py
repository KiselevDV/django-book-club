from django.contrib import admin

from .models import Category, Genre, Topic, Author, Publisher, Book, BookExcerpt, RatingStar, \
    Rating, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookExcerpt)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)

# Описываем модели которые хотим зарегистрировать и выводить в админке
# Register your models here.
