# Generated by Django 4.2.4 on 2023-09-02 22:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0004_alter_factory_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="factory",
            old_name="status",
            new_name="active",
        ),
    ]
