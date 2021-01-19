from django.contrib import admin
from .models import Todo, Books

# Register your models here.
admin.site.register(Todo)
admin.site.register(Books)