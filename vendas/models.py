# Django
from django.db import models

# Signals
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# Models
from clientes.models import Person
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField()
    
    def __str__(self):
        return self.numero

    # def get_total(self):
    #     total = 0
    #     for produto in self.produtos.all():
    #         total += produto.preco

    #     self.valor = (total - self.desconto) + self.impostos
    #     self.save()

    #     return self.valor


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.FloatField(default=1)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.venda} - {self.produto}({self.quantidade})'


# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_totals(sender, instance, *args, **kwargs):
    instance.get_total()

# m2m_changed.connect(update_totals, sender=Venda.produtos.through)