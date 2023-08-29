# Generated by Django 4.2.4 on 2023-08-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Checkpoints",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("checkpoint_location", models.CharField(max_length=150)),
                ("coordinates", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="CurrencyRates",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pair_name", models.CharField(max_length=10)),
                ("rate", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="HappyCustomers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=50)),
                ("company_link", models.URLField()),
                (
                    "company_logo",
                    models.ImageField(blank=True, null=True, upload_to="static/logos/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Options",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marge", models.FloatField()),
                ("delta_for_offer_update", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Countries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country_region", models.CharField(max_length=50)),
                ("rate_eur_per_km", models.FloatField()),
                ("minimal_rate", models.IntegerField()),
                ("additional_expences", models.IntegerField()),
                (
                    "checkpoints",
                    models.ManyToManyField(blank=True, to="main.checkpoints"),
                ),
            ],
        ),
    ]