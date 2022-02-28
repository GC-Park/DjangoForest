
# SECURITY WARNING: keep the secret key used in production secret!
mySECRET_KEY = 'django-insecure-(dvirz1sk@=m7-e1+fbg*s7#p!e(+=e3xu=tmvul(a6si*zwjf'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

myDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'mysql',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : '127.0.0.1',
        'PORT' : '3309',
    }
}
