from .base import *

ALLOWED_HOSTS = ["greatproject.com",]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'greatproject-production',
        'USER': 'greatproject',
        'PASSWORD': 'UXeVnzNiy72mV9',
		'HOST': '127.0.0.1',
		'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}