# Generated by Django 4.2.4 on 2023-08-27 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0001_initial"),
        ("logistics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distancecalculator",
            name="start_point",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="goods.factory"
            ),
        ),
    ]
