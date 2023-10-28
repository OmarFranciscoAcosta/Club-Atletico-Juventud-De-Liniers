from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChangeLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Asócialo a tu modelo de usuario si lo tienes
    description = models.TextField()

    class Meta:
        verbose_name = 'Registro de Cambio'
        verbose_name_plural = 'Registros de Cambios'
        ordering = ['-date']