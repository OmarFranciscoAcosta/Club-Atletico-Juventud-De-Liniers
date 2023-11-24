from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CAJL$club-atletico-juventud-de-liniersdb',
        'USER': 'CAJL',
        'PASSWORD': 'clubatleticojuventuddeliniers',
        'HOST': 'CAJL.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

#VARIABLES DE REDIRECCION DE LOGIN Y LOGOUT
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

PASSWORD_RESET_COMPLETE_URL = 'password_reset_complete'

#CONFIGURACION DE EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "contactocmsoftware@gmail.com"
EMAIL_HOST_PASSWORD = "tkxffxjaadqeviik"
