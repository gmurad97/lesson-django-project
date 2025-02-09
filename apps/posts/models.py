from django.db import models
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=150, unique=True, null=False, blank=False, verbose_name="Name"
    )
    slug = models.SlugField(
        max_length=150, unique=True, null=False, blank=True, verbose_name="Slug"
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pages:category_articles", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)


class Article(models.Model):
    title = models.CharField(
        max_length=255, unique=True, null=False, blank=False, verbose_name="Title"
    )
    slug = models.SlugField(
        max_length=255, unique=True, null=False, blank=True, verbose_name="Slug"
    )
    description = models.TextField(null=False, blank=False, verbose_name="Description")
    poster = models.ImageField(
        upload_to="articles/%Y/%m/%d/",
        default="articles/default.png",
        null=False,
        blank=True,
        verbose_name="Poster",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        null=False,
        blank=False,
        verbose_name="Category",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages:news_detail", kwargs={"article_slug": self.slug})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ("-created_at",)
