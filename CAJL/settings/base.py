from pathlib import Path


LENGUAGE_CODE = "es-AR"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_TZ = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'


# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
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
    'CAJL.aplications.vouchers',
    'CAJL.aplications.partnersXactivities',
    'CAJL.aplications.voucherspartnersXactivities',
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
LANGUAGES = [
    ('es', 'Spanish'),
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_TZ = True

WSGI_APPLICATION = 'CAJL.wsgi.application'
