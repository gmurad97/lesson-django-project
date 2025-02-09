from django.db import models
from django.urls import reverse
# Create your models here.



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
