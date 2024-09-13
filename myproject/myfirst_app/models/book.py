from django.db import models
from django.core.validators import MinLengthValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(
        max_length=200,
        null=True,
        blank=False,
        error_messages={
            'blank': 'Поле не может быть пустым'
        },
        validators=[MinLengthValidator(5)]
    )
    published_date = models.DateField()
    website = models.URLField(null=True, blank=True)

    GENRE_CHOICES = [
        ('fantasy', 'Fantasy'),
        ('love', 'Love'),
        ('science', 'Science')
    ]
    genre = models.CharField(
        max_length=10, null=True,
        choices=GENRE_CHOICES,
        default='no genre'  # Update default to one of the choices
    )
    themes = models.CharField(unique_for_date='published_date',
                              max_length=100,
                              default='No themes')
    description = models.TextField(max_length=500,
                                   null=True)
    net_worth = models.BigIntegerField(null=True)
    positive_review = models.PositiveIntegerField(null=True)
    rating = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 null=True)


#

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100,
                            verbose_name="Имя")
    email = models.EmailField(max_length=100, unique=True,
                              help_text="введите мэйл",
                              db_index=True, null=True)
    website = models.URLField(max_length=100)
    age = models.IntegerField(null=True)
    net_worth = models.BigIntegerField(null=True)
    positive_review = models.PositiveIntegerField(null=True)
    rating = models.DecimalField(max_digits=10,
                                 decimal_places=3,
                                 null=True)
    last_updated = models.DateField(auto_now=True,
                                    null=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      null=True,
                                      help_text='Время создания записи')
    duration = models.DurationField(null=True)
    # upload_file = models.FileField(upload_to="postert/", help_text='Загрузите постер фильма')
    enter_time = models.TimeField(null=True,
                                  auto_now=True)
