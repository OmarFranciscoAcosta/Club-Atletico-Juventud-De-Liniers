from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import payments
from CAJL.aplications.changelog.models import ChangeLog
from .translations import MODEL_TRANSLATIONS

@receiver([post_save, post_delete], sender=payments)
def create_change_log(sender, instance, **kwargs):
    # Determina si la acción es una creación o eliminación
    if 'created' in kwargs:
        created = kwargs['created']
    else:
        created = False

    if created:
        action = 'Creado'
    else:
        action = 'Eliminado' if kwargs.get('signal') == post_delete else 'Actualizado'

    user = instance.user # Asegúrate de que el campo de relación con el usuario esté correctamente configurado

    model_name = MODEL_TRANSLATIONS.get(sender.__name__, sender.__name__)

    ChangeLog.objects.create(
        model_name=model_name,
        user=user,
        description=f'{action} - ID: {instance.id}'
    )