# Generated by Django 4.2.4 on 2023-09-02 22:17

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inquiry", "0002_alter_customer_email"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inquiry",
            options={"get_latest_by": "order_date"},
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=16, region=None, verbose_name="phone number"
            ),
        ),
    ]
