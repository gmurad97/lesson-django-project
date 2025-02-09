from django.db import models
from django.urls import reverse

# Create your models here.

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
