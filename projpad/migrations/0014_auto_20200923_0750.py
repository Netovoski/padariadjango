# Generated by Django 3.0.6 on 2020-09-23 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projpad', '0013_auto_20200922_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_produto',
            name='data',
            field=models.DateField(default=datetime.date(2020, 9, 23)),
        ),
    ]
