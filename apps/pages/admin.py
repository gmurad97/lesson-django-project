from django.contrib import admin
from .models import Category, Article

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "status"]
    list_display_links = ["name"]
    list_editable = ["status"]
    search_fields = ["name"]
    ordering = ["-created_at"]
    list_per_page = 10
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at", "updated_at", "status"]
    list_display_links = ["title"]
    list_editable = ["status"]
    search_fields = ["title", "description"]
    ordering = ["-created_at"]
    list_per_page = 10
    readonly_fields = ["created_at", "updated_at"]
