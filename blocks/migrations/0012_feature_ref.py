# Generated by Django 4.2.7 on 2024-07-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0011_additionalcatalogblock_add_annotation_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="ref",
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name="ссылка"),
        ),
    ]
