# Generated by Django 3.1.2 on 2020-10-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201016_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
