# Generated by Django 4.2.7 on 2024-06-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0007_site_domain"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="subdomain",
            field=models.CharField(max_length=50, unique=True, verbose_name="поддомен"),
        ),
    ]