# Generated by Django 3.0.6 on 2020-10-27 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0008_auto_20201022_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='fkvenda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venda_produto',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
