# Generated by Django 2.0.1 on 2020-01-30 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0003_auto_20200130_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField(default=1)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemsdopedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itemsdopedido',
            name='venda',
        ),
        migrations.DeleteModel(
            name='ItemsDoPedido',
        ),
    ]
