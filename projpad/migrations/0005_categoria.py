# Generated by Django 3.0.6 on 2020-08-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projpad', '0004_funcionario_resumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
