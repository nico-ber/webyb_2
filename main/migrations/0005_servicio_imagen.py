# Generated by Django 3.1.4 on 2021-01-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210108_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
