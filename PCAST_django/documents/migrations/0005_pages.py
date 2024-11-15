# Generated by Django 4.2.5 on 2023-09-26 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0004_alter_legacysubjects_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quartex_image_iiif_hash",
                    models.CharField(max_length=36, unique=True),
                ),
                ("order", models.IntegerField()),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="documents.document",
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "document")},
            },
        ),
    ]