# Generated by Django 2.1.7 on 2019-04-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0002_auto_20190429_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='pickup_date',
            field=models.DateField(),
        ),
    ]