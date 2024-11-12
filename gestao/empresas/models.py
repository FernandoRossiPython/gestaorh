from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True, help_text='Nome da Empresa')

    def __str__(self):
        return str(self.nome)