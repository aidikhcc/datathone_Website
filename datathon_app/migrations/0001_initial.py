# Generated by Django 5.1.4 on 2024-12-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Participant",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=20)),
                ("nationality", models.CharField(max_length=50)),
                (
                    "event_choice",
                    models.CharField(
                        choices=[
                            ("datathon", "Datathon Only"),
                            ("workshop", "Workshop Only"),
                            ("both", "Both Events"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("confirmed", "Confirmed"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "skills",
                    models.TextField(
                        help_text="Comma-separated list of skills (e.g., Python, R, Statistics)"
                    ),
                ),
                ("slack_username", models.CharField(blank=True, max_length=50)),
                ("discord_username", models.CharField(blank=True, max_length=50)),
                ("linkedin", models.URLField(blank=True)),
                ("twitter", models.CharField(blank=True, max_length=50)),
                ("wadi_rum_trip", models.BooleanField(default=False)),
                ("falafel_dinner", models.BooleanField(default=False)),
                ("kickboxing_session", models.BooleanField(default=False)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-registration_date"],
            },
        ),
        migrations.CreateModel(
            name="Sponsor",
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
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(upload_to="sponsor_logos/")),
                ("website", models.URLField()),
                ("description", models.TextField()),
                (
                    "tier",
                    models.CharField(
                        choices=[
                            ("platinum", "Platinum"),
                            ("gold", "Gold"),
                            ("silver", "Silver"),
                            ("bronze", "Bronze"),
                        ],
                        max_length=10,
                    ),
                ),
                ("contact_person", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=254)),
                ("contact_phone", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["tier", "name"],
            },
        ),
    ]
