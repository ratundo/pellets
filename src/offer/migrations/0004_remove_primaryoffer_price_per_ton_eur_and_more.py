# Generated by Django 4.2.4 on 2023-08-28 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logistics", "0003_alter_distancecalculator_end_point"),
        ("goods", "0002_alter_factory_goods_alter_factory_uah_eur_rate"),
        ("main", "0001_initial"),
        ("offer", "0003_remove_primaryoffer_price_fca_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="primaryoffer",
            name="price_per_ton_eur",
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
            name="factories",
            field=models.ManyToManyField(
                blank=True, related_name="factories", to="goods.factory"
            ),
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="marge",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="primary_offer_marge",
                to="main.options",
            ),
        ),
    ]
