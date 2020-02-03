# Django
from django.db import models
from django.db.models import Sum, F, FloatField, Min, Max, Avg, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desconto(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def minimo(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def maximo(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def numero_pedidos(self):
        return self.all().aggregate(Count('id'))['id__count']

    def pedidos_enviados(self):
        # print(f'OBJECT: {object.produto}')
        print(f'MODEL: {self.model.produto}')
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']