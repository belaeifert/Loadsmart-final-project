# Generated by Django 2.1.7 on 2019-04-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0002_auto_20190416_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrieruser',
            name='MC_number',
            field=models.IntegerField(max_length=8, verbose_name='MC number'),
        ),
    ]
