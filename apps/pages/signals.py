from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.pages.models.advertising import Advertising
from .models import *



@receiver(pre_delete, sender=Advertising)
def delete_file(sender, instance, **kwargs):
    if (
        hasattr(instance, "poster")
        and instance.poster
        and instance.poster.name not in ["articles/default.png", "sliders/default.png"]
    ):
        instance.poster.delete(save=False)
    elif hasattr(instance, "image") and instance.image:
        instance.image.delete(save=False)