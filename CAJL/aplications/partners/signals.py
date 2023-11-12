from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import partners
from CAJL.aplications.changelog.models import ChangeLog
from .translations import MODEL_TRANSLATIONS

@receiver([post_save, post_delete], sender=partners)
def create_change_log(sender, instance, **kwargs):
    action = 'Creado' if kwargs.get('created') else 'Eliminado' if kwargs.get('signal') == post_delete else 'Actualizado'

    user = getattr(instance, 'user', None)

    model_name = MODEL_TRANSLATIONS.get(sender.__name__, sender.__name__)

    try:
        # Crear el registro en cualquier caso
        ChangeLog.objects.create(
            model_name=model_name,
            user=user,
            description=f'{action} - ID: {instance.id}'
        )

    except Exception as e:
        print(f"Error creating ChangeLog: {e}")