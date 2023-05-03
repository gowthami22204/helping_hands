# Generated by Django 4.1.7 on 2023-05-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Login_out",
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
                ("username", models.CharField(max_length=100)),
                ("session_id", models.CharField(max_length=100)),
                ("login_date", models.DateTimeField(auto_now_add=True)),
                ("logout_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mycred",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("passcode", models.CharField(max_length=100)),
                ("password", models.CharField(default="", max_length=100)),
                ("is_Donar", models.BooleanField(default=False, verbose_name="Donar")),
                (
                    "is_Volunteer",
                    models.BooleanField(default=False, verbose_name="Volunteer"),
                ),
                ("is_Admin", models.BooleanField(default=False, verbose_name="Admin")),
                ("is_Staff", models.BooleanField(default=False, verbose_name="Staff")),
                ("roles", models.CharField(default="0", max_length=100)),
                (
                    "Areaofinterest",
                    models.CharField(
                        choices=[
                            ("1", "medical camps"),
                            ("2", "feed_needy"),
                            ("3", "campaings"),
                            ("4", "Amanuensis_scribe"),
                            ("5", "animal_husbandry"),
                            ("6", "others"),
                        ],
                        default="1",
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
            ],
        ),
    ]