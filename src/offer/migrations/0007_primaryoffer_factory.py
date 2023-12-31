# Generated by Django 4.2.4 on 2023-08-28 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0002_alter_factory_goods_alter_factory_uah_eur_rate"),
        ("offer", "0006_remove_primaryoffer_price_fca_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="primaryoffer",
            name="factory",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="goods.factory",
            ),
            preserve_default=False,
        ),
    ]
