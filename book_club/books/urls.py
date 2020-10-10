from django.urls import path

from . import views


urlpatterns = [
    path("", views.BooksView.as_view()),
    # slug это то что передано в get() в модуле views.py
    path('<slug:slug>/', views.BookDetailView.as_view())
]

# URL приложения
