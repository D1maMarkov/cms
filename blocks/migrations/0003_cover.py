# Generated by Django 4.2 on 2024-04-25 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0002_exampleblock_button_ref_exampleblock_button_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('button_text', models.CharField(max_length=20, null=True, verbose_name='Текст кнопки')),
                ('button_ref', models.CharField(max_length=20, null=True, verbose_name='Ссылка для кнопки')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('image_desctop', models.ImageField(upload_to='images/covers/', verbose_name='Картинка(десктоп)')),
                ('image_mobile', models.ImageField(upload_to='images/covers/', verbose_name='Картинка(смартфон)')),
                ('second_button_text', models.CharField(max_length=20, null=True, verbose_name='Текст второй кнопки')),
                ('second_button_ref', models.CharField(max_length=20, null=True, verbose_name='Ссылка для второй кнопки')),
                ('block_relation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blocks.blockrelationship')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.template', verbose_name='html шаблон')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
