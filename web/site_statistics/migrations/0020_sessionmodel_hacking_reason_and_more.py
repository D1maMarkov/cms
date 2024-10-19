# Generated by Django 5.0 on 2024-09-28 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0019_alter_sessionaction_options_alter_useraction_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionmodel",
            name="hacking_reason",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="useractivity",
            name="hacking_reason",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name="GoToThePage",
        ),
    ]