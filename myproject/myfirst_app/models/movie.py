

from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='Directors Name')

    def __repr__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Movie Title')
    default_director = Director.objects.get(id=1)
    directors = models.ForeignKey(Director,
                                  on_delete=models.DO_NOTHING,
                                  DEFAULT='None',
                                  related_name='movies')

    def __repr__(self):
        return self.title
