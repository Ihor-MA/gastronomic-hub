# Generated by Django 4.2.5 on 2023-10-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0007_alter_cook_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.PositiveIntegerField(default=3),
        ),
    ]
