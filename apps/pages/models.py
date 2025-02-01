from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name="Title")
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(
        upload_to="articles/%Y/%m/%d/", null=True, blank=True, verbose_name="Image"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Category",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]
