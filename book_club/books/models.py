from datetime import date

from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=30)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=50)
    description = models.TextField("Описание жанра")
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Tag(models.Model):
    """Темы"""
    name = models.CharField("Тема", max_length=150)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Publisher(models.Model):
    """Издатель"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Об издателе", blank=True)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


class Translator(models.Model):
    """Переводчики"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Переводчик"
        verbose_name_plural = "Переводчики"


class Author(models.Model):
    """Авторы"""
    name = models.CharField("Имя", max_length=100)
    date_of_birth = models.DateField("Дата рождения", blank=True)
    description = models.TextField("Об авторе", blank=True)
    image = models.ImageField("Аватарка", upload_to="authors/", blank=True)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Книги"""
    title = models.CharField("Название", max_length=80)
    description = models.TextField("О книге")
    cover = models.ImageField("Обложка", upload_to="books/")
    year_of_writing = models.PositiveSmallIntegerField("Год написания", default=2020, blank=True)
    year_of_publishing = models.PositiveSmallIntegerField("Год издания", default=2020)
    date_receipt = models.DateField("Дата поступления", default=date.today)
    isbn = models.IntegerField(
        "Номер книги", null=True, blank=True,
        help_text="Международный стандартный номер книги ISBN (EAN)")
    signs = models.FloatField(
        "Знаков", blank=True, null=True, help_text="Количество знаков (тысяч)")
    pages = models.PositiveSmallIntegerField("Количество страниц")
    writer = models.ForeignKey(
        Author, verbose_name="Писатель", related_name="book_writer", on_delete=models.CASCADE)
    translator = models.ManyToManyField(
        Translator, verbose_name="Переводчик", related_name="book_translator", blank=True)
    publisher = models.ManyToManyField(
        Publisher, verbose_name="Издательство", related_name="book_publisher")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    tags = models.ManyToManyField(Tag, verbose_name="Темы")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    age = models.CharField("Возрастной ценз", max_length=3,
                           choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'),
                                    ('14+', '14+'), ('16+', '16+'), ('18+', '18+')],
                           default='0+')
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookExcerpt(models.Model):
    """Отрывок из книги"""
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отрывок из книги"
        verbose_name_plural = "Отрывки из книги"


class RatingStar(models.Model):
    """Звёзды рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звёзды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Quote(models.Model):
    """Цитаты"""
    text = models.TextField("Цитата", max_length=1000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    date_receipt = models.DateField("Дата создания", default=date.today)

    def __str__(self):
        return self.book

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Отзыв", max_length=10000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    date_receipt = models.DateField("Дата создания", default=date.today)

    def __str__(self):
        return f'{self.name} - {self.book}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

# Описание таблиц в базе данных
# Create your models here.
