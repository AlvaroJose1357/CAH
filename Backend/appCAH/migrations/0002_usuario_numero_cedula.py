# Generated by Django 4.2.3 on 2023-07-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCAH', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='numero_cedula',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
