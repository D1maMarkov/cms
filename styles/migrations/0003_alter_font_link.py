# Generated by Django 4.2 on 2024-04-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("styles", "0002_alter_font_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="font",
            name="link",
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Ссылка для подключения"),
        ),
    ]
