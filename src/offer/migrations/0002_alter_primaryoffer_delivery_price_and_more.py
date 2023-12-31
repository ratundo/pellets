# Generated by Django 4.2.4 on 2023-08-28 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logistics", "0003_alter_distancecalculator_end_point"),
        ("main", "0001_initial"),
        ("offer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primaryoffer",
            name="delivery_price",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="distance",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="primary_offer_distance",
                to="logistics.distancecalculator",
            ),
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="marge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="primary_offer_marge",
                to="main.options",
            ),
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="price_dap",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="price_fca",
            field=models.FloatField(blank=True),
        ),
    ]
