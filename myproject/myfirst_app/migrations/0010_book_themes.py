# Generated by Django 5.1.1 on 2024-09-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirst_app', '0009_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='themes',
            field=models.CharField(default='No themes', max_length=100, unique_for_date='published_date'),
        ),
    ]
