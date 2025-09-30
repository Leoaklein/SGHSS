from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPOS = [
        ('paciente', 'Paciente'),
        ('profissional', 'Profissional'),
        ('Admin', "Administrador")
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)