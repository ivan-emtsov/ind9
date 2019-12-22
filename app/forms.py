"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    functionality = forms.ChoiceField(
        label='Оцените функциональность сайта',
        choices=[
            ('1', 'Отлично'),
            ('2', 'Хорошо'),
            ('3', 'Удовлетворительно'),
            ('4', 'Неудовлетворительно')
        ],
        widget=forms.RadioSelect,
        initial=1
    )
    design = forms.ChoiceField(
        label='Оцените дизайн сайта',
        choices=[
            ('1', 'Отлично'),
            ('2', 'Хорошо'),
            ('3', 'Удовлетворительно'),
            ('4', 'Неудовлетворительно')
        ],
        initial=1
    )
    notice = forms.BooleanField(label='Получать новости сайта по e-mail?', required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Пожелания', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Комментарий'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title', 'description', 'content', 'posted', 'author', 'image'}
        labels = {'title': 'Заголовок', 'description': 'Краткое описание', 'content': 'Содержание', 'posted': 'Дата', 'author': 'Автор', 'image': 'Путь к картинке'}