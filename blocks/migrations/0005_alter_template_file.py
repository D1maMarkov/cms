# Generated by Django 4.2 on 2024-05-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0004_alter_contentblock_image1_alter_contentblock_image2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="template",
            name="file",
            field=models.CharField(max_length=50, verbose_name="Название файла (например base.html)"),
        ),
    ]
