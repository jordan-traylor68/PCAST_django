# Generated by Django 5.0.2 on 2024-05-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0019_alter_document_quartexyn_delete_quartexyn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controlledsubjects',
            options={'verbose_name_plural': 'New Subjects'},
        ),
        migrations.RemoveField(
            model_name='document',
            name='controlledsubjects',
        ),
        migrations.AddField(
            model_name='document',
            name='controlledsubjects',
            field=models.ManyToManyField(to='documents.controlledsubjects'),
        ),
    ]