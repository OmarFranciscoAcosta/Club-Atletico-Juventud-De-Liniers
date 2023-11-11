from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from changelog.models import ChangeLog

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Si el usuario fue recién creado
        description = f"Se creó el usuario: {instance.username}"
        ChangeLog.objects.create(model_name='User', user=instance, description=description)