from django.contrib import admin
# Import your models here.
from .models import Book

# Register your models here.
admin.site.register(Book)