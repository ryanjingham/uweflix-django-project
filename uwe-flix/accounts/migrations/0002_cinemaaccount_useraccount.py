# Generated by Django 4.1.5 on 2023-03-22 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CinemaAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="accounts.account",
                    ),
                ),
            ],
            bases=("accounts.account",),
        ),
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="accounts.account",
                    ),
                ),
            ],
            bases=("accounts.account",),
        ),
    ]