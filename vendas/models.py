# Django
from django.db import models
from django.db.models import Sum, F, FloatField, Max

# Signals
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver

# Models
from clientes.models import Person
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produto = models.ManyToManyField(Produto, through='ItemDoPedido')
    nfe_emitida = models.BooleanField()
    
    def __str__(self):
        return self.numero

    def update_totals(self):
        """Solicitamos un nuevo cálculo de los totales para 
        posteriormente actualizar la bd"""
        self.get_total()


    def get_total(self):
        """Calculamos el total de todos los productos, con sus cantidades,
        descuentos por producto, descuento por la compra general y además,
        incluimos los impuestos..."""

        tot = self.itemdopedido_set.all().aggregate(
            tot_ped = Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0

        tot = (tot + float(self.impostos)) - float(self.desconto)
        Venda.objects.filter(id=self.id).update(valor=tot)


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.FloatField(default=1)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.venda} - {self.produto}({self.quantidade})'


@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total(sender, instance, *args, **kwargs):
    instance.venda.get_total()

@receiver(post_save, sender=Venda)
def update_vendas_total2(sender, instance, *args, **kwargs):
    instance.get_total()

@receiver(post_delete, sender=ItemDoPedido)
def update_vendas_total3(sender, instance, *args, **kwargs):
    instance.venda.get_total()


# @receiver(m2m_changed, sender=Venda.produto.through)
# def update_vendas_total2(sender, instance, action, *args, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         instance.get_total()

