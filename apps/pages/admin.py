""" from django.utils.html import format_html
from django.contrib import admin

from apps.pages.models.advertising import Advertising
from apps.pages.models.contact import Contact
from apps.pages.models.setting import Setting
from apps.pages.models.slider import Slider
from apps.pages.models.faq import Faq
from .models import *

# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "title",
        # "description",
        "link_tag",
        "created_at",
        "updated_at",
        "status",
    )
    list_display_links = ("title",)
    list_editable = ("status",)
    list_per_page = 20
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "description", "link")
    readonly_fields = ("image_tag", "created_at", "updated_at")

    fieldsets = (
        ("Main Settings", {"fields": ("title", "description", "link","poster", "status")}),
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

    @admin.display(description="Link")
    def link_tag(self, obj):
        return format_html("<a href='{}' target='_blank'>🔗{}</a>", obj.link, obj.link)

    class Media:
        css = {
            "all": ("pages/css/lity.min.css",),
        }
        js = ("pages/js/lity.min.js",)


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "__str__",
        "link_tag",
        "created_at",
        "updated_at",
    )
    list_display_links = ("__str__",)
    readonly_fields = ("image_tag", "created_at", "updated_at")

    fieldsets = (
        ("Main Settings", {"fields": ("image", "link", "status")}),
        ("General Information", {"fields": ("image_tag", "created_at", "updated_at")}),
    )

    @admin.display(description="Image")
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                "<a href='{}' data-lity><img style='width:48px;height:48px;border-radius:50%;object-fit:cover;object-position:center center;' src='{}'></a>",
                obj.image.url,
                obj.image.url,
            )

    @admin.display(description="Link")
    def link_tag(self, obj):
        return format_html("<a href='{}' target='_blank'>🔗{}</a>", obj.link, obj.link)

    def has_add_permission(self, request):
        return not Advertising.objects.exists()

    class Media:
        css = {
            "all": ("pages/css/lity.min.css",),
        }
        js = ("pages/js/lity.min.js",)


@admin.register(Faq)
class Faq(admin.ModelAdmin):
    list_display = (
        "question",
        "created_at",
        "updated_at",
        "status",
    )
    list_display_links = ("question",)
    list_editable = ("status",)
    list_per_page = 20
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("answer", "question")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Main Settings", {"fields": ("question", "answer", "status")}),
        ("General Information", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email_tag",
        "subject",
        "created_at",
        "updated_at",
    )
    list_display_links = ("name",)
    list_per_page = 20
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Contact Information",
            {"fields": ("name", "email_tag", "subject", "message")},
        ),
        ("General Information", {"fields": ("created_at", "updated_at")}),
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    @admin.display(description="Email")
    def email_tag(self, obj):
        return format_html("<a href='mailto:{}'>{}</a>", obj.email, obj.email)


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
 """