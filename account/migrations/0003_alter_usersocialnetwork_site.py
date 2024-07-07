# Generated by Django 4.2.7 on 2024-07-05 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0009_alter_site_online_from"),
        ("account", "0002_usersocialnetwork"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersocialnetwork",
            name="site",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="socials",
                to="domens.site",
                verbose_name="сайт",
            ),
        ),
    ]