from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_ad = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)
    is_favorites = models.BooleanField(default=False)