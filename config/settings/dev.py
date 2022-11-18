from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p00469_scfreiburg',
        'USER': 'root',
        'PASSWORD': '123456',
		'HOST': '127.0.0.1',
		'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}