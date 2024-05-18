# Generated by Django 4.2 on 2024-05-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("username", models.CharField(max_length=100, verbose_name="Имя пользователя")),
                ("phone", models.CharField(max_length=12, verbose_name="Номер телефона")),
                ("email", models.CharField(max_length=200, null=True, verbose_name="E-main")),
                ("new_email", models.CharField(blank=True, max_length=200, null=True, verbose_name="новый E-main")),
                ("email_is_confirmed", models.BooleanField(default=False, verbose_name="Почта подтверждена")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="пользователь создан")),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
