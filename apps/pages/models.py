from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,verbose_name="Название")
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Article(models.Model):
    title = models.CharField()
    description = models.TextField()
    poster = models.ImageField()
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()










