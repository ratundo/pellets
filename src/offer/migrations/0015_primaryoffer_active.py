# Generated by Django 4.2.4 on 2023-09-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("offer", "0014_alter_primaryoffer_distance"),
    ]

    operations = [
        migrations.AddField(
            model_name="primaryoffer",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
