# Generated by Django 3.2.9 on 2021-11-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0005_auto_20211111_1512'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
