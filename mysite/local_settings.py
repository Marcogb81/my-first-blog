import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'marco',
        'PASSWORD': 'diariomarco', # psql -c "ALTER USER marco WITH PASSWORD 'diariomarco'"
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True