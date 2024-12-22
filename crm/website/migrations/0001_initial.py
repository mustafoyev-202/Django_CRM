# Generated by Django 5.1.4 on 2024-12-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
            ],
        ),
    ]
