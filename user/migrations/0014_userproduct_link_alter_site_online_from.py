# Generated by Django 4.2 on 2024-08-25 13:43

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0013_userproduct_comment_userproduct_connected_with_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userproduct",
            name="link",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(default=datetime.datetime(2024, 8, 25, 13, 43, 36, 317026), verbose_name="онлайн с"),
        ),
    ]
