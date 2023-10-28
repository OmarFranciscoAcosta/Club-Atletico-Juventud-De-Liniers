from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from CAJL.aplications.activities.models import activities
from CAJL.aplications.changelog.models import ChangeLog

@receiver([post_save, post_delete], sender=activities)
def create_change_log(sender, instance, **kwargs):
    if 'created' in kwargs:
        created = kwargs['created']
    else:
        created = False

    if created:
        action = 'Creado'
    else:
        action = 'Eliminado' if kwargs.get('signal') == post_delete else 'Actualizado'

    user = instance.user  # Asegúrate de que el campo de relación con el usuario esté correctamente configurado

    ChangeLog.objects.create(
        model_name=sender.__name__,
        user=user,  # Accede al usuario relacionado en tu modelo
        description=f'{action} - ID: {instance.id}'
    )