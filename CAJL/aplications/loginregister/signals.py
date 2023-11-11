from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from CAJL.aplications.changelog.models import ChangeLog


signal_connected = False  # Variable para rastrear si la señal está conectada

@receiver(post_save, sender=User, dispatch_uid="unique_user_created")
def user_created(sender, instance, created, **kwargs):
    global signal_connected  # Usa la variable global

    if not signal_connected:
        if created:
            description = f"Se creó el usuario: {instance.username}"
            print("Senial ejecutada")
            ChangeLog.objects.create(model_name='User', user=instance, description=description)

        signal_connected = True  # Establece la variable a True después de ejecutar la señal