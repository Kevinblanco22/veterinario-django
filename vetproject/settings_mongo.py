from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'veterinaria_db',   
        'CLIENT': {
            'host': "mongodb://localhost:27017",
        }
    }
}
