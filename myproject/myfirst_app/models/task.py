from django.db import models
from django.db.models import ManyToManyField, DateField
from datetime import datetime


class Category(models.Model):
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Task(models.Model):
    description = models.CharField(max_length=100, verbose_name='Описание задачи')
    title = models.CharField(max_length=100, unique_for_date='title', verbose_name='Название задачи')
    categories = models.ManyToManyField(Category)
    STATUS_CHOICE = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    Blocked = models.CharField(max_length=100, choices=STATUS_CHOICE)
    deadline = DateField(max_length=100, default=datetime.today)
    created_at = DateField(max_length=100, auto_now_add=True)


class SubTask(models.Model):
    description = models.CharField(max_length=100, verbose_name='Отдельная часть основной задачи (Task)')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    STATUS_CHOICE = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICE)
    deadline = DateField(default=datetime.today)
    created_at = DateField(auto_now_add=True)
