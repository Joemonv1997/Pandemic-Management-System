# Generated by Django 4.0.3 on 2022-04-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0003_district"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
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
                ("Hospital", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "District",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.district",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
                ("Name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "Hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.hospital",
                    ),
                ),
            ],
        ),
    ]
