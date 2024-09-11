from django.db import models
from django.core.validators import MinLengthValidator


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              error_messages={'blank': 'Поле обязательно к заполнению (*)'},
                              validators=[MinLengthValidator(5)])
    published_date = models.DateField()
    website = models.URLField(null=True, blank=True)
    GERNE_CHOICE = [
        ('Fantasy', 'Fantasy'),
        ('Love', 'Love'),
        ('science', 'Science'),
        ('history', 'History'),
    ]
    genre = models.CharField(max_length=10, choices=GERNE_CHOICE, default='No genre')
    themes = models.CharField(unique_for_date='published_date', max_length=100, default='No themes')


class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100, verbose_name="Имя")
    email = models.EmailField(max_length=100, help_text="Введите email*", db_index=True)
    website = models.URLField(max_length=100, help_text='Введите website*', editable=True,
                              error_messages={'blank': 'Поле обязательно к заполнению (*)'})
