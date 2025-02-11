from django.db import models

class Estado(models.Model): 
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    
    def __str__ (self):
        return f"{self.nome} ({self.sigla})"
    
    class Meta: 
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__ (self):
        return f"{self.nome} ({self.estado.sigla})"
    
    class Meta: 
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    dataNascimento= models.DateField
    cidade=models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__ (self):
        return f"{self.nome} ({self.cidade.nome}/{self.cidade.estado.sigla})"
    
    class Meta: 
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
