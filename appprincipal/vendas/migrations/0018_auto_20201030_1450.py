# Generated by Django 3.0.6 on 2020-10-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0017_auto_20201030_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='multtotal',
            field=models.FloatField(editable=False),
        ),
    ]
