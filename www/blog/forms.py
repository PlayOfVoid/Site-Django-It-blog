from django import forms
from .models import Comment  # Замените .models на ваш модуль models

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        # Виджеты можно настроить здесь для более детального контроля
        # Например, добавить классы CSS
        widgets = {
            'author': forms.TextInput(attrs={'class': 'comment-author-input'}),
            'text': forms.Textarea(attrs={'class': 'comment-text-area'}),
        }