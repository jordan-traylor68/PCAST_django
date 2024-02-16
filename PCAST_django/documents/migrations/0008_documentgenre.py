# Generated by Django 5.0.2 on 2024-02-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20240126_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Document Genres',
            },
        ),
    ]