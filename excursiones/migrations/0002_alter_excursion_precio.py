# Generated by Django 4.2.3 on 2023-08-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='precio',
            field=models.PositiveIntegerField(verbose_name='precio'),
        ),
    ]
