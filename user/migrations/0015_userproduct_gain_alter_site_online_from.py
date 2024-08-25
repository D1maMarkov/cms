# Generated by Django 4.2 on 2024-08-25 14:05

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0014_userproduct_link_alter_site_online_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="userproduct",
            name="gain",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(default=datetime.datetime(2024, 8, 25, 14, 5, 34, 979136), verbose_name="онлайн с"),
        ),
    ]
