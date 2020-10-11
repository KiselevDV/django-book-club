from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksView.as_view(), name='head_page'),
    # slug это то что передано в get() в модуле views.py
    path('<slug:slug>/', views.AboutBookView.as_view(), name="about_book"),
    path('<slug:slug>/read-excerpt/', views.BookExcerptView.as_view(), name='book_read_excerpt'),
]

# URLs приложения
