from django.db import models
from django.urls import reverse

# Create your models here.


class Setting(models.Model):
    snow_mode = models.BooleanField(default=False, verbose_name="Snow Mode")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    github = models.URLField(blank=True, null=True, verbose_name="Github")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return "Site Settings"

    def get_absolute_url(self):
        return reverse("pages:home")

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
