# Generated by Django 4.2 on 2024-07-21 16:29

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0031_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 21, 16, 29, 25, 707168, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]
