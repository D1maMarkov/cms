# Generated by Django 4.2 on 2024-08-12 20:15

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0006_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 8, 12, 20, 15, 3, 300966, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]