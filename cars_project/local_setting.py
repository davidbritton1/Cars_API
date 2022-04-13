# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^6l06z@wk=k@t&-hwb)=_ae@c4l*j1tw)^iwn2xnk25w66-%qa'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}