# Generated by Django 4.2 on 2024-05-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_user_email_is_confirmed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="new_email",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="новый E-main"),
        ),
    ]