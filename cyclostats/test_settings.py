from settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'ATOMIC_REQUESTS': True
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
