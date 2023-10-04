# Generated by Django 4.2.5 on 2023-10-04 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0004_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(5)],
            ),
        ),
        migrations.AlterField(
            model_name="dishtype",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
