# Generated by Django 3.1.8 on 2023-04-29 19:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0005_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="score",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]
            ),
        ),
    ]
