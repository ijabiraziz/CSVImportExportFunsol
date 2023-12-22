from django.contrib import admin
from .models import Author, Book, Genre

#Register all models to access them on Admin panel
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)

