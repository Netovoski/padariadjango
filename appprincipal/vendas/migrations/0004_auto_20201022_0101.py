# Generated by Django 3.0.6 on 2020-10-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20201022_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='precovenda',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='venda_produto',
            name='quantidade',
            field=models.FloatField(),
        ),
    ]
