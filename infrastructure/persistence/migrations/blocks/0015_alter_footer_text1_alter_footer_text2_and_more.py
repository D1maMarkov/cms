# Generated by Django 5.0 on 2024-10-25 02:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0014_alter_navmenuitem_navbar_footer_footermenuitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer",
            name="text1",
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="footer",
            name="text2",
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="footer",
            name="text3",
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]