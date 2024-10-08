# Generated by Django 5.1.1 on 2024-09-12 20:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirst_app', '0012_author_created_at_author_duration_author_enter_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Описание задачи')),
                ('title', models.CharField(max_length=100, unique_for_date='title', verbose_name='Название задачи')),
                ('Blocked', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], max_length=100)),
                ('deadline', models.DateField(default=datetime.datetime.today, max_length=100)),
                ('created_at', models.DateField(auto_now_add=True, max_length=100)),
                ('categories', models.ManyToManyField(to='myfirst_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Отдельная часть основной задачи (Task)')),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], max_length=100)),
                ('deadline', models.DateField(default=datetime.datetime.today)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfirst_app.task')),
            ],
        ),
    ]
