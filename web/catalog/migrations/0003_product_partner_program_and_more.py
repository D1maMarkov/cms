# Generated by Django 4.2 on 2024-08-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_product_terms_of_the_promotion"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="partner_program",
            field=models.CharField(
                choices=[
                    ("Приведи друга", "Приведи друга"),
                    ("CPA сеть", "CPA сеть"),
                    ("Друзья/CPA", "Друзья/CPA"),
                    ("Только админ", "Только админ"),
                    ("Нет", "Нет"),
                ],
                max_length=100,
                null=True,
                verbose_name="Партнерская программа",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="verification_of_registration",
            field=models.BooleanField(default=False),
        ),
    ]
