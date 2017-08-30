import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '!^--%1qp4klkqr0yvlnfg=d$&#=@_nkzp78_b0kfd1!52peo0v'

DEBUG = True

ALLOWED_HOSTS = ['mahalii.herokuapp.com']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mahali.apps.MahaliConfig',
    'django.contrib.gis',
    'leaflet',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fridah.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'fridah.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Define A POSTGIS database
        'NAME': "fridah",
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    },
}

db_from_env = dj_database_url.config()

if db_from_env:
    DATABASES['default'].update(db_from_env)
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")

# Define Leaflet maps configurations
LEAFLET_CONFIG = {
    'TILES': 'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', #Tiles to be used
    'DEFAULT_CENTER': (-1.09713135, 37.014170107681),
    'DEFAULT_ZOOM': 13,
}
