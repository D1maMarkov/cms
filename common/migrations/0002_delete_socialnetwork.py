# Generated by Django 4.2 on 2024-08-21 18:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0009_delete_userfont_alter_usermessanger_messanger_and_more"),
        ("blocks", "0003_alter_additionalcatalogblock_options_and_more"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SocialNetwork",
        ),
    ]
