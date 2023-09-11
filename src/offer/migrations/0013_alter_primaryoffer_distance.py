# Generated by Django 4.2.4 on 2023-08-31 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logistics", "0003_alter_distancecalculator_end_point"),
        ("offer", "0012_alter_primaryoffer_distance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primaryoffer",
            name="distance",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="offer_distances",
                to="logistics.distancecalculator",
            ),
        ),
    ]
