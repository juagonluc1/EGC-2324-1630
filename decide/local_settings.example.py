ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://10.5.0.1:8001',
    'base': 'http://10.5.0.1:8001',
    'booth': 'http://10.5.0.1:8001',
    'census': 'http://10.5.0.1:8001',
    'mixnet': 'http://10.5.0.1:8001',
    'postproc': 'http://10.5.0.1:8001',
    'store': 'http://10.5.0.1:8001',
    'visualizer': 'http://10.5.0.1:8001',
    'voting': 'http://10.5.0.1:8001',
}

BASEURL = 'http://10.5.0.1:8001'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql,
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
