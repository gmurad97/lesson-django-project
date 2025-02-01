from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Article


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["preview", "name", "created_at", "updated_at", "status"]
    list_display_links = ["name"]
    list_filter = ["status", "created_at", "updated_at"]
    list_editable = ["status"]
    search_fields = ["name"]
    ordering = ["-created_at"]
    list_per_page = 10
    readonly_fields = ["created_at", "updated_at", "preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}" data-lity><img style="width:50px;height:50px;border-radius:50%;object-fit:cover;object-position:center center;" src="{obj.image.url}"></a>'
            )
        return "No Image"

    class Media:
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/lity@2.4.1/dist/lity.min.css"],
        }
        js = ["https://cdn.jsdelivr.net/npm/lity@2.4.1/dist/lity.min.js"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "preview",
        "title",
        "category",
        "created_at",
        "updated_at",
        "status",
    ]
    list_filter = ["category", "status", "created_at", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["status"]
    search_fields = ["title", "description"]
    ordering = ["-created_at"]
    list_per_page = 10
    readonly_fields = ["created_at", "updated_at", "preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}" data-lity><img style="width:50px;height:50px;border-radius:50%;object-fit:cover;object-position:center center;" src="{obj.image.url}"></a>'
            )
        return "No Image"

    class Media:
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/lity@2.4.1/dist/lity.min.css"],
        }
        js = ["https://cdn.jsdelivr.net/npm/lity@2.4.1/dist/lity.min.js"]
