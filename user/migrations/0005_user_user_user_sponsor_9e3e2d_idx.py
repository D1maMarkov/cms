# Generated by Django 4.2 on 2024-08-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_user_test_user_test_set_alter_user_sponsor"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["sponsor_id"], name="user_user_sponsor_9e3e2d_idx"),
        ),
    ]