from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'


# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'crispy_forms',
    'crispy_bootstrap5',
    'bootstrap_datepicker_plus',
    'django.contrib.admin',
    'django_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local apps
    'CAJL.aplications.loginregister',
    'CAJL.aplications.partners',
    'CAJL.aplications.location',
    'CAJL.aplications.activities',
    'CAJL.aplications.prices',
    'CAJL.aplications.payments',
    'CAJL.aplications.changelog',
]

JAZZMIN_SETTINGS = {
    # Configuración del logo
    "site_title": "Club Atlético Juventud de Liniers",
    "site_logo": "images/LogoEscudo.png",  # Ruta al archivo de imagen del logo
    "site_icon": "images/LogoEscudo.ico",  # Ruta al archivo de imagen del icono
    "welcome_sign": "Bienvenido al panel de Administración del club!",
    "copyright": "CM SOFTWARE",
}


CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'CAJL.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'CAJL$club-atletico-juventud-de-liniersdb',
#         'USER': 'CAJL',
#         'PASSWORD': 'clubatleticojuventuddeliniers',
#         'HOST': 'CAJL.mysql.pythonanywhere-services.com',
#         'PORT': '3306',
#     }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Directorios desde los cuales recolectar los archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'staticfiles']


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



LANGUAGES = [
    ('es', 'Spanish'),
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_TZ = True

WSGI_APPLICATION = 'CAJL.wsgi.application'
