from django.apps import AppConfig


class PartnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CAJL.aplications.partners'

    def ready(self):
        import CAJL.aplications.partners.signals