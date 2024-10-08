# Generated by Django 4.2 on 2024-08-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlockRelationship",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("block_name", models.CharField(max_length=50, unique=True, verbose_name="Имя компонента")),
                ("block", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Блок",
                "verbose_name_plural": "Блоки",
                "ordering": ["block_name"],
            },
        ),
    ]
