from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import partners
from CAJL.aplications.changelog.models import ChangeLog

@receiver(post_save, sender=partners)
@receiver(post_delete, sender=partners)

def create_change_log(sender, instance, created, **kwargs):
    if created:
        action = 'Creado'
    else:
        action = 'Actualizado' if sender.objects.filter(pk=instance.pk).exists() else 'Eliminado'
    
    ChangeLog.objects.create(
        model_name=sender.__name__,
        user=instance.user,  # Asegúrate de ajustar esto según cómo obtienes al usuario
        description=f'{action} - ID: {instance.id}'
    )