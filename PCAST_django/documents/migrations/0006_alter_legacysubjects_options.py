# Generated by Django 4.2.5 on 2023-11-13 20:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0005_pages"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="legacysubjects",
            options={"verbose_name_plural": "Legacy Subjects"},
        ),
    ]
