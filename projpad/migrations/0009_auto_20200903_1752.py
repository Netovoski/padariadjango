# Generated by Django 3.0.6 on 2020-09-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projpad', '0008_auto_20200903_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='precoprod',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
