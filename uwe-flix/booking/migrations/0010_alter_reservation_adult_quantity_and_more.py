# Generated by Django 4.1.7 on 2023-05-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_reservation_reservee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='adult_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='child_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='student_quantity',
            field=models.IntegerField(default=0),
        ),
    ]