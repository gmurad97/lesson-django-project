from django.db import models
from django.urls import reverse

# Create your models here.

class Slider(models.Model):
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Title"
    )
    description = models.TextField(null=False, blank=False, verbose_name="Description")
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    poster = models.ImageField(
        upload_to="sliders/",
        default="sliders/default.png",
        null=False,
        blank=True,
        verbose_name="Poster",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering = ("-created_at",)