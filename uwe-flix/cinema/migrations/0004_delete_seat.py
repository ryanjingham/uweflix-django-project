# Generated by Django 4.1.5 on 2023-03-17 02:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0003_alter_seat_reserved"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Seat",
        ),
    ]