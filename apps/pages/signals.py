from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import *


@receiver(pre_delete, sender=Article)
@receiver(pre_delete, sender=Slider)
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


@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Article)
def update_slug(sender, instance, **kwargs):
    if not instance.slug or (instance.pk and instance.name != instance.slug):
        instance.slug = slugify(
            instance.name if hasattr(instance, "name") else instance.title
        )
