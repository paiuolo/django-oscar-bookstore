from django.test import TestCase

# Utils
def crea_modello(model, **kwargs):
    m = model()
    for key, val in kwargs.items():
        setattr(m,key,val)
    m.save()
    return m