# Generated by Django 5.0.6 on 2024-11-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legacysubjects',
            name='name',
            field=models.TextField(blank=True, unique=True),
        ),
    ]
