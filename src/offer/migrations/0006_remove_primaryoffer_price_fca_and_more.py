# Generated by Django 4.2.4 on 2023-08-28 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inquiry", "0001_initial"),
        ("offer", "0005_remove_primaryoffer_factories_primaryoffer_price_fca_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="primaryoffer",
            name="price_fca",
        ),
        migrations.AlterField(
            model_name="primaryoffer",
            name="inquiry",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="primary_offer",
                to="inquiry.inquiry",
            ),
        ),
    ]
