# Generated by Django 4.2.6 on 2023-10-24 00:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_project_modified_at_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, null=True, upload_to="projects/images/%Y/%m/%d/%H/%M/%S'"), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, default=list, size=None),
        ),
    ]
