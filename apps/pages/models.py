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


class Faq(models.Model):
    question = models.TextField(null=False, blank=False, verbose_name="Question")
    answer = models.TextField(null=False, blank=False, verbose_name="Answer")
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ("-created_at",)


class Contact(models.Model):
    name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name="First Name"
    )
    email = models.EmailField(
        max_length=255, blank=False, null=False, verbose_name="Email"
    )
    subject = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Subject"
    )
    message = models.TextField(blank=False, null=False, verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ("-created_at",)


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
