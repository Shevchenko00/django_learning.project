from django.contrib import admin
from .models.book import Book, Author
from .models.movie import Director, Movie



admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Book)
admin.site.register(Author)