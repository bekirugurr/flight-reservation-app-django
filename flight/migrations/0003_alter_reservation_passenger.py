# Generated by Django 4.0.5 on 2022-06-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_alter_passenger_first_name_alter_passenger_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ManyToManyField(related_name='reservations', to='flight.passenger'),
        ),
    ]
