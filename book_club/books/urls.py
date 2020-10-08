from django.urls import path

from . import views


urlpatterns = [
    path("", views.BooksView.as_view())
]

# URL приложения
