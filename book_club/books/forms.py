from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Review  # от какой модели буде строить форму
        fields = ("name", "email", "text")  # поля из модели которые будут в форме

# Формы к приложению
