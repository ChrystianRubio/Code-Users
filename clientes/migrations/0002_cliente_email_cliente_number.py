# Generated by Django 4.2.6 on 2023-10-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='example@.com', max_length=80),
        ),
        migrations.AddField(
            model_name='cliente',
            name='number',
            field=models.CharField(default='55 55555-5555', max_length=20),
        ),
    ]
