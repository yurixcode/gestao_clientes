# Generated by Django 2.0.1 on 2018-03-19 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20180318_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('view_task', 'Can see available tasks'), ('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed'))},
        ),
    ]