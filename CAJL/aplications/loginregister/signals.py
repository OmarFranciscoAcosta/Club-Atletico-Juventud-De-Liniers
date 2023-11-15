from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from CAJL.aplications.changelog.models import ChangeLog
from .translations import MODEL_TRANSLATIONS

def user_created(sender, instance, created, **kwargs):
    if created:
        # Registro en el changelog
        model_name = MODEL_TRANSLATIONS.get(sender.__name__, sender.__name__)
        description = f"Se creó el usuario: {instance.username}"
        ChangeLog.objects.create(model_name=model_name, user=instance, description=description)

        # Asignación automática al grupo
        group_name = "Administrativo"  # Reemplaza con el nombre de tu grupo
        try:
            group = Group.objects.get(name=group_name)
            if not instance.groups.filter(name=group_name).exists():
                instance.groups.add(group)
        except Group.DoesNotExist:
            pass  # Maneja la lógica si el grupo no existe