from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from CAJL.aplications.changelog.models import ChangeLog
from .translations import MODEL_TRANSLATIONS

signal_connected = False  # Variable para rastrear si la señal está conectada

@receiver(post_save, sender=User, dispatch_uid="unique_user_created")
def user_created(sender, instance, created, **kwargs):
    global signal_connected  # Usa la variable global

    if not signal_connected:
        if created:
            # Registro en el changelog
            
            model_name = MODEL_TRANSLATIONS.get(sender.__name__, sender.__name__)
            
            description = f"Se creó el usuario: {instance.username}"
            ChangeLog.objects.create(model_name=sender.__name__, user=instance, description=description)

            # Asignación automática al grupo
            group_name = "Administrativo"  # Reemplaza con el nombre de tu grupo
            group, created = Group.objects.get_or_create(name=group_name)
            instance.groups.add(group)

        signal_connected = True  # Establece la variable a True después de ejecutar la señal