from django.db import models
from django.urls import reverse


class Advertising(models.Model):
    image = models.ImageField(
        upload_to="advertising/",
        null=False,
        blank=False,
        verbose_name="Image",
    )
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return "Advertising"

    class Meta:
        verbose_name = "Advertising"
        verbose_name_plural = "Advertisements"
        ordering = ("-created_at",)
