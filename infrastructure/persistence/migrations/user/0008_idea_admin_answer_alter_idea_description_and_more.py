# Generated by Django 5.0 on 2024-09-08 02:13

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_alter_idea_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="idea",
            name="admin_answer",
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True, verbose_name="Ответ"),
        ),
        migrations.AlterField(
            model_name="idea",
            name="description",
            field=models.TextField(max_length=1000, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="idea",
            name="finishe_date",
            field=models.DateField(null=True, verbose_name="Срок"),
        ),
        migrations.AlterField(
            model_name="idea",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "Новое"),
                    ("in_pregress", "В работе"),
                    ("planned", "Запланировано"),
                    ("done", "Реализовано"),
                    ("reject", "Отклонено"),
                    ("repeat", "Повтор"),
                ],
                default="new",
                max_length=100,
                verbose_name="статус",
            ),
        ),
        migrations.AlterField(
            model_name="idea",
            name="title",
            field=models.CharField(max_length=60, verbose_name="Тема"),
        ),
        migrations.AlterField(
            model_name="user",
            name="sponsor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sponsors",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Спонсор",
            ),
        ),
    ]