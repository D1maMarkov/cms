# Generated by Django 4.2 on 2024-08-23 03:47

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(default=datetime.datetime(2024, 8, 23, 3, 47, 3, 720197), verbose_name="онлайн с"),
        ),
    ]
