# Generated by Django 4.2 on 2024-07-28 11:10

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0039_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 28, 11, 10, 4, 484730, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]
