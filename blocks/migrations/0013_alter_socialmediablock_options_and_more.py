# Generated by Django 4.2 on 2024-05-12 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0012_socialmediablock_socialmediabutton"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="socialmediablock",
            options={"verbose_name": "Блок подписок на соц сети", "verbose_name_plural": "Блоки подписок на соц сети"},
        ),
        migrations.AlterField(
            model_name="socialmediabutton",
            name="block",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="buttons", to="blocks.socialmediablock"
            ),
        ),
    ]
