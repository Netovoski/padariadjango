# Generated by Django 3.0.6 on 2020-10-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0015_auto_20201030_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='multtotal',
            field=models.FloatField(editable=False, null=True),
        ),
    ]