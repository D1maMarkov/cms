# Generated by Django 4.2 on 2024-09-02 01:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="text",
            field=ckeditor.fields.RichTextField(max_length=300000, verbose_name="Содержание"),
        ),
    ]
