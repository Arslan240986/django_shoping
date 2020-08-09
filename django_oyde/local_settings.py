import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pv&oz33&r1t9zg*%2o=au*)-=-@g4l@ii6zj#twow$h-o)@juz'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_oyden',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]