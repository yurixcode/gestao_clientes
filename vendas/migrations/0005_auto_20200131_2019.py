# Generated by Django 2.0.1 on 2020-01-31 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0004_auto_20200130_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='produto',
            field=models.ManyToManyField(through='vendas.ItemDoPedido', to='produtos.Produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='impostos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]