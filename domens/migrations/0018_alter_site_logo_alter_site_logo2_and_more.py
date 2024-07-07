# Generated by Django 4.2.7 on 2024-07-07 17:49

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domens", "0017_alter_site_online_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images/logo", verbose_name="Лого"),
        ),
        migrations.AlterField(
            model_name="site",
            name="logo2",
            field=models.ImageField(blank=True, null=True, upload_to="images/logo", verbose_name="Лого для форм"),
        ),
        migrations.AlterField(
            model_name="site",
            name="logo_width",
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name="ширина лого"),
        ),
        migrations.AlterField(
            model_name="site",
            name="logo_width_mobile",
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name="ширина лого(мобильный)"),
        ),
        migrations.AlterField(
            model_name="site",
            name="online_from",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 7, 17, 49, 28, 841798, tzinfo=datetime.timezone.utc),
                verbose_name="онлайн с",
            ),
        ),
    ]
