from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .models import Book

@receiver(post_save, sender=Book)
def create_hex_code(sender, instance, created, **kwargs):
    if created:
        # Generate a unique hex code
        hex_code = uuid.uuid4().hex[:6].upper()
        # Print the hex code for the newly created Book instance
        print(f"Hex code for book '{instance}': {hex_code}")