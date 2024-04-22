# Generated by Django 4.2 on 2024-04-21 13:40

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Цвет')),
                ('font', models.CharField(max_length=15, verbose_name='Шрифт для текста')),
                ('fontWeight', models.CharField(max_length=15, verbose_name='Толщина текста')),
                ('fontWeightMobile', models.CharField(max_length=15, verbose_name='Толщина текста(мобильный)')),
                ('fontSize', models.CharField(max_length=15, verbose_name='Размер текста')),
                ('fontSizeMobile', models.CharField(max_length=15, verbose_name='Размер текста(мобильный)')),
                ('fontColorInverted', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Инвертированный цвет текста')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовок',
            },
        ),
        migrations.CreateModel(
            name='MainText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Цвет')),
                ('font', models.CharField(max_length=15, verbose_name='Шрифт для текста')),
                ('fontWeight', models.CharField(max_length=15, verbose_name='Толщина текста')),
                ('fontWeightMobile', models.CharField(max_length=15, verbose_name='Толщина текста(мобильный)')),
                ('fontSize', models.CharField(max_length=15, verbose_name='Размер текста')),
                ('fontSizeMobile', models.CharField(max_length=15, verbose_name='Размер текста(мобильный)')),
                ('fontColorInverted', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Инвертированный цвет текста')),
            ],
            options={
                'verbose_name': 'Основной текст',
                'verbose_name_plural': 'Основной текст',
            },
        ),
    ]
