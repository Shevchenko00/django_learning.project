from django.contrib import admin
from .models.book import Book, Author
from .models.movie import Director, Movie
# from .models.task import Book2, Author
from .models.task import Category, Task, SubTask

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(SubTask)
admin.site.register(Category)
admin.site.register(Task)
