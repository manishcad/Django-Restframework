# Generated by Django 4.2.6 on 2023-10-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_model',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Files'),
        ),
    ]
