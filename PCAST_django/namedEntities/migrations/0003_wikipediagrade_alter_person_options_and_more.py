# Generated by Django 4.2.5 on 2023-12-04 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namedEntities', '0002_persondocumentrole_alter_country_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikipediaGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id'], 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='wikipedia_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='namedEntities.wikipediagrade'),
        ),
    ]
