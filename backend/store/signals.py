
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db import transaction

from .models import Product


@receiver(pre_save, sender=Product)
def delete_old_product_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_product = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return

    old_image = old_product.image
    new_image = instance.image

    if old_image and old_image.name != getattr(new_image, 'name', None):
        storage = old_image.storage
        old_image_name = old_image.name

        transaction.on_commit(
            lambda: storage.delete(old_image_name)
        )


@receiver(post_delete, sender=Product)
def delete_product_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        storage = instance.image.storage
        image_name = instance.image.name

        transaction.on_commit(
            lambda: storage.delete(image_name)
        )
