from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug_with_link",
        "created_at",
        "updated_at",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 20
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("name", "slug")
    readonly_fields = ("created_at", "updated_at")
    exclude = ("slug",)

    fieldsets = (
        ("Main Settings", {"fields": ("name", "status")}),
        ("General Information", {"fields": ("created_at", "updated_at")}),
    )

    @admin.display(description="Slug Link")
    def slug_with_link(self, obj):
        return format_html(
            "<a href='{}' target='_blank'>🔗{}</a>", obj.get_absolute_url(), obj.slug
        )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "title_tag",
        "slug_with_link",
        "category_tag",
        "created_at",
        "updated_at",
        "status",
    )
    list_display_links = ("title_tag",)
    list_editable = ("status",)
    list_per_page = 20
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "slug")
    readonly_fields = ("image_tag", "created_at", "updated_at")
    exclude = ("slug",)

    fieldsets = (
        (
            "Main Settings",
            {"fields": ("title", "description", "category", "poster", "status")},
        ),
        ("General Information", {"fields": ("image_tag", "created_at", "updated_at")}),
    )

    @admin.display(description="Poster")
    def image_tag(self, obj):
        if obj.poster:
            return format_html(
                "<a href='{}' data-lity><img style='width:48px;height:48px;border-radius:50%;object-fit:cover;object-position:center center;' src='{}'></a>",
                obj.poster.url,
                obj.poster.url,
            )

    @admin.display(description="Slug Link")
    def slug_with_link(self, obj):
        sliced_slug = obj.slug if len(obj.slug) <= 16 else obj.slug[:16] + "..."
        return format_html(
            "<a href='{}' target='_blank'>🔗{}</a>", obj.get_absolute_url(), sliced_slug
        )

    @admin.display(description="Category")
    def category_tag(self, obj):
        # temporary change this please
        edit_url = f"/admin/{obj.category._meta.app_label}/{obj.category._meta.model_name}/{obj.category.pk}/"
        return format_html("<a href='{}'>{}</a>", edit_url, obj.category)

    @admin.display(description="Title")
    def title_tag(self, obj):
        sliced_title = obj.title if len(obj.title) <= 16 else obj.title[:16] + "..."
        return format_html("{}", sliced_title)

    class Media:
        css = {
            "all": ("pages/css/lity.min.css",),
        }
        js = ("pages/js/lity.min.js",)
