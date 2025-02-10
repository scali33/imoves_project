from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    TIPO_USUARIO = [
        ('vendedor', 'Vendedor'),
        ('comprador', 'Comprador'),
    ]
    
    email = models.EmailField(unique=True)  # Evita nulos e valores em branco
    name = models.CharField(max_length=200, blank=True, null=True)  # Opcional
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, default='comprador')
    USERNAME_FIELD = 'email'
    numero = models.CharField(max_length=20, blank=True, null=True)
    REQUIRED_FIELDS = ['username']  # 'username' ainda é necessário para criar superusers corretamente

    def __str__(self):
        return self.email
        


class Casa(models.Model):
    endereco = models.CharField(unique=True, max_length=300)
    regiao_cidade = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Melhor que FloatField para valores monetários
    aluga = models.BooleanField(default=False)  # Para garantir um valor padrão
    aluguel_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    metros_quadrados = models.PositiveIntegerField()  # Evita números negativos
    descricao = models.TextField()
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Corrigindo typo e adicionando blank=True
    created = models.DateTimeField(auto_now_add=True)  # Melhor usar auto_now_add para data de criação

    def __str__(self):
        return f"{self.endereco} - {self.regiao_cidade}"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'comprador'})  # Só compradores podem favoritar
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.name} favoritou {self.casa.endereco}"

class ImageCasa(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name="imagens")
    image = models.ImageField(upload_to='casa_images/')