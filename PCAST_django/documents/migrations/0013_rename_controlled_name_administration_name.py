# Generated by Django 5.0.2 on 2024-03-19 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0012_alter_document_documentgenre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administration',
            old_name='controlled_name',
            new_name='name',
        ),
    ]