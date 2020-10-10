from django.contrib import admin

from .models import Category, Genre, Tag, Translator, Author, Publisher, Book, BookExcerpt, \
    RatingStar, Quote, Rating, Review

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Publisher)
admin.site.register(Translator)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookExcerpt)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Quote)
admin.site.register(Review)

# Описываем модели которые хотим зарегистрировать и выводить в админке
# Register your models here.
