from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_ad = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)