# Generated by Django 3.0.6 on 2020-10-22 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendas', '0002_auto_20201022_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='fkfuncionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venda_produto',
            name='precovenda',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
