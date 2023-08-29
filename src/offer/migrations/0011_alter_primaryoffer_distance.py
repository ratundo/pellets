# Generated by Django 4.2.4 on 2023-08-28 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logistics", "0003_alter_distancecalculator_end_point"),
        ("offer", "0010_primaryoffer_factory_primaryoffer_photos_and_more"),
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