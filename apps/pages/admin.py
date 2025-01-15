from django.contrib import admin
from .models import News,Comments

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","description")
    list_filter = ("id","title")
    # list_editable = ("title","description")

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","comment_text","news")
    list_filter = ("id","first_name","last_name","comment_text")