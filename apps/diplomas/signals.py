import os
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save
from .models import Issuer


@receiver(pre_save, sender=Issuer)
def issuer_update(sender, instance, **kwargs):
    """
    Replacing the specific image and thumbnail of a issuer after update
    """
    if instance.created:

        if sender.objects.get(pk=instance.pk).image:
            old_image = sender.objects.get(pk=instance.pk).image
            new_image = instance.image
            if not old_image == new_image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        if sender.objects.get(pk=instance.pk).image_thumb:
            old_thumb = sender.objects.get(pk=instance.pk).image_thumb
            new_thumb = instance.image_thumb
            if not old_thumb == new_thumb:
                if os.path.isfile(old_thumb.path):
                    os.remove(old_thumb.path)


@receiver(pre_delete, sender=Issuer)
def issuer_delete(sender, instance, **kwargs):
    """
    Deleting the specific image and thumbnail of a issuer after delete it
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.image_thumb:
        if os.path.isfile(instance.image_thumb.path):
            os.remove(instance.image_thumb.path)
