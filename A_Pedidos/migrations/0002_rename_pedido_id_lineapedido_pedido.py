# Generated by Django 5.0.7 on 2024-07-23 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A_Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
    ]
