# Generated by Django 4.1.5 on 2023-04-23 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0013_remove_cinema_ticket_price_showing_adult_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="showing",
            name="social_distancing",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="Seat",
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
                ("seat_number", models.CharField(max_length=10)),
                ("is_available", models.BooleanField(default=True)),
                (
                    "showing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seats",
                        to="cinema.showing",
                    ),
                ),
            ],
        ),
    ]