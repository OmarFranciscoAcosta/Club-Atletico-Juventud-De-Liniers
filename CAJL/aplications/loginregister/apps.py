from django.apps import AppConfig


class LoginregisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CAJL.aplications.loginregister'

def ready(self):
        import CAJL.aplications.loginregister.signals