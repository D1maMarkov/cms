# Generated by Django 4.2 on 2024-08-15 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_tests", "0001_initial"),
        ("user", "0003_user_sponsor"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.BooleanField(default=False, verbose_name="тестовый пользователь"),
        ),
        migrations.AddField(
            model_name="user",
            name="test_set",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="site_tests.testuserset"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="sponsor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Спонсор",
            ),
        ),
    ]