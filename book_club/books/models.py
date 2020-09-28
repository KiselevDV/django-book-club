from datetime import date

from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=30)
    description = models.CharField("Описание", max_length=300)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    """Авторы и переводчики"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Аватарка", upload_to="authors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Авторы и переводчики"
        verbose_name_plural = "Авторы и переводчики"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=80)
    tagline = models.CharField("Слоган", max_length=80, blank=True, null=True)
    description = models.TextField("Описание")
    cover = models.ImageField("Обложка", upload_to="books/")
    year_of_writing = models.PositiveSmallIntegerField("Год написания", default=2020)
    year_of_publishing = models.PositiveSmallIntegerField("Год издания", default=2020)
    date_receipt = models.PositiveSmallIntegerField("Дата поступления", default=date.today)
    isbn = models.IntegerField(
        "Номер книги", help_text="Международный стандартный номер книги", unique=True)
    signs = models.PositiveIntegerField("Количество знаков", blank=True, null=True)
    pages = models.PositiveSmallIntegerField("Количество страниц")
    writers = models.ManyToManyField(
        Author, verbose_name="Писатель", related_name="book_writer")
    translators = models.ManyToManyField(
        Author, verbose_name="Переводчик", related_name="book_translator", blank=True)
    illustrators = models.ManyToManyField(
        Author, verbose_name="Иллюстратор", related_name="book_illustrator", blank=True)
    publisher = models.CharField("Издательство", max_length=80)
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    age = models.CharField("Возрастной ценз", max_length=3,
                           choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'),
                                    ('14+', '14+'), ('16+', '16+'), ('18+', '18+')],
                           default='0+')
    cost = models.PositiveIntegerField("Стоимость книги")
    url = models.SlugField(max_length=120, unique=True)
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
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=10000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

# Описание таблиц в базе данных
# Create your models here.
