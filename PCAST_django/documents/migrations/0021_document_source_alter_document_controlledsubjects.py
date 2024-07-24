# Generated by Django 5.0.6 on 2024-07-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0020_alter_controlledsubjects_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='controlledsubjects',
            field=models.ManyToManyField(blank=True, to='documents.controlledsubjects'),
        ),
    ]
