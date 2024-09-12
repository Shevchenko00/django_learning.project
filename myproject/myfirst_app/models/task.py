# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.db import models
# from datetime import date
#
#
# from django.db import models
# from datetime import date
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     birst_day = models.DateField(null=True, default=date.today)
#     profile = models.URLField(null=True, blank=True)
#     deleted = models.BooleanField(default=False, verbose_name="Удален")
#     rating = models.FloatField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
#
#
# class Book2(models.Model):
#     name = models.CharField(max_length=20)
#     author = models.ForeignKey(Author ,on_delete=models.DO_NOTHING, related_name='book2')
#     published_data = models.DateField()
