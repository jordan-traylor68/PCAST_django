# Generated by Django 5.0.2 on 2024-03-19 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0012_alter_document_documentgenre_and_more'),
        ('namedEntities', '0006_alter_areaofstudy_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionDocumentRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Institution Document Roles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InstitutionDocumentRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.document')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='namedEntities.institution')),
                ('part_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='namedEntities.sector')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='namedEntities.persondocumentrole')),
            ],
        ),
    ]