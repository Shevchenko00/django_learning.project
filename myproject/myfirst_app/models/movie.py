from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20, verbose_name='Director\'s Name')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Movie Title')
    directors = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='movies', null=True, blank=True)

    def __str__(self):
        return self.title
