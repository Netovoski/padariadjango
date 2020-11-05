# Generated by Django 3.0.6 on 2020-10-22 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda_produto',
            name='fkfuncionario',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venda_produto',
            name='precovenda',
            field=models.FloatField(),
        ),
    ]
