# Generated by Django 4.1.7 on 2023-04-14 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistCont', '0024_alter_catalogocuentas_cuenta_mayor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocuentas',
            name='nivel',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3')], null=True),
        ),
    ]