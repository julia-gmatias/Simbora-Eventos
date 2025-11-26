import uuid
from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from datetime import date

class Eventos(models.Model):
    id_evento = models.IntegerField (
        primary_key=True
    )

    imagem_url = models.URLField (
        blank=True,
        null=True,
    )

    titulo = models.CharField (
        max_length=50,
        blank=True,
        null=True,
    )

    descricao = models.CharField (
        max_length=500,
        blank=True,
        null=True,
    )

    data_evento = models.DateField (
        validators=[MinValueValidator(date.today())]
    )

    #adicionar data de fim do evento

    status = models.CharField (
        max_length=30, 
        choices=[
            ('INICIADO', 'Evento iniciado'), 
            ('EM_ANDAMENTO', 'Evento em andamento'), 
            ('FINALIZADO', 'Evento já finalizado'),
        ],
        blank=True,
        null=True, 
    )

    participantes = models.IntegerField (
        validators=[
            MinValueValidator(3),
            MaxValueValidator(20)
        ],
    )

    data_criacao = models.DateTimeField (
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField (
        auto_now=True
    )

'''   
   id_endereco = models.ForeignKey (
        'core.Endereco',
        on_delete=models.PROTECT,
        related_name='eventos',
        blank=True,
        null=True,
    )

    id_categoria = models.ForeignKey (

    ) 
'''
