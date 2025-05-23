# Generated by Django 5.2 on 2025-04-18 03:45

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
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150)),
                ("phone", models.IntegerField(max_length=20)),
                ("address", models.CharField(max_length=300)),
                ("city", models.CharField(max_length=255)),
                ("province", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=120)),
            ],
        ),
    ]
