from .base import *

DEBUG = True
ALLOWED_HOSTS = ["test.greatproject.com",]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'greatproject-test',
        'USER': 'greatproject',
        'PASSWORD': 'UXeVnzNiy72mV9',
		'HOST': '127.0.0.1',
		'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}