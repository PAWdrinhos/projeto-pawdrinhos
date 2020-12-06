from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from localflavor.br.forms import BRCNPJField, BRCPFField, BRZipCodeField, BRStateChoiceField



class Usuario(AbstractUser):

    class Suit(models.IntegerChoices):
        Ong = 1
        Padrinho = 2
        
    name        = models.CharField(max_length=255)
    documento   = models.CharField(max_length=20, null=True, unique=True)
    state       = models.CharField(max_length=50, null=True)
    city        = models.CharField(max_length=100, null=True)
    cep         = models.CharField(max_length=10, null=True)
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=255)
    tipo        = models.IntegerField(choices = Suit.choices)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

class Animal(models.Model):

    class Suit(models.IntegerChoices):
        Cão = 1
        Gato = 2

    nome        = models.CharField(max_length=255)
    classe      = models.IntegerField(choices = Suit.choices)
    desc        = models.TextField()
    padrinho    = models.ForeignKey(Usuario, null=True, blank=True ,on_delete=models.CASCADE, related_name='PADRINHO')
    ong         = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ONG')
    created_at  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name   
