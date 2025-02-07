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
    pass


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Setting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Faq)
class Faq(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    list_display_links = ("__str__",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Main Settings", {"fields": ("snow_mode",)}),
        ("Social Network", {"fields": ("instagram", "github", "linkedin")}),
        ("General Information", {"fields": ("created_at", "updated_at")}),
    )

    def has_add_permission(self, request):
        return not Setting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
