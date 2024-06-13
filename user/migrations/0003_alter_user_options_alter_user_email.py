# Generated by Django 4.2.7 on 2024-06-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_user_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=200, null=True, verbose_name="E-mail"),
        ),
    ]