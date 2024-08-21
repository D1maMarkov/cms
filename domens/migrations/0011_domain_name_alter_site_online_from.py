# Generated by Django 4.2 on 2024-08-17 17:08

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0010_site_created_at_alter_site_online_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="domain",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 8, 17, 17, 8, 2, 53820, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]