# Generated by Django 4.2 on 2024-09-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0002_alter_document_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="name",
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Загаловок для пользователей"),
        ),
    ]
