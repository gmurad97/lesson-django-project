from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name="Заголовок")
    status = models.BooleanField(default=True, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


# class Article(models.Model):
#     title = ""
#     description = ""
#     image = ""
#     category = ""
#     status = ""
#     created_at = ""
#     updated_at = ""
