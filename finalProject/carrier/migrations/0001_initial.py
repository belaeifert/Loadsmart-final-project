# Generated by Django 2.1.7 on 2019-04-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('MC_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('id_shipper', models.IntegerField()),
                ('id_carrier', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
