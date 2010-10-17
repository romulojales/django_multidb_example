from django.db import models
from django_multibd import MultiBdManager
# Create your models here.


class Principal(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

class Auxiliar(models.Model):

    _default_manager =	MultiBdManager("auxiliar")
#    _base_manager   =	MultiBdManager("auxiliar")
#    objects = MultiBdManager("auxiliar")
    class Meta:
        managed = False
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
