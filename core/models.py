
from django.db import models
from django.contrib import admin
from email.policy import default
# Create your models here.

class buracos(models.Model): 
  GRAVIDADE_CHOICES=[
    ["Leve", "Leve"],
    ["Moderado", "Moderado"],
    ["Critico", "Crítico"]
  ]
  STATUS_CHOICES=[
    ["Nao Consertado", "Não Consertado"],
    ["Consertado", "Consertado"]
  ]
  bu_quantia = models.IntegerField("Quantia", blank=False, null=False, default=1)
  bu_gravidade = models.CharField("Gravidade", choices=GRAVIDADE_CHOICES, max_length=100)
  bu_rua = models.CharField("Rua", max_length=255, blank=False, null=False) 
  bu_bairro = models.CharField("Bairro", max_length=255, blank=False, null=False)
  bu_status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default="Não Consertado")
  class Meta:
    verbose_name_plural = "Buracos"
  def __str__(self):
    return self.bu_bairro

class buracos_status(admin.ModelAdmin): 
  list_display = ['bu_rua', 'bu_bairro', 'bu_status']