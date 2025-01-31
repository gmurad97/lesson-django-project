from django.contrib import admin
from .models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


""" @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass """


""" Release django template fully ^)
news/1
news/2

categories/slug*/all news datas
categories/
 """
