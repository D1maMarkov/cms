# Generated by Django 4.2.7 on 2024-07-09 14:13

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0020_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 9, 14, 13, 18, 54597, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]
