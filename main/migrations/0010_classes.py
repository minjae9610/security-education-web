# Generated by Django 4.1.2 on 2022-11-04 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0009_alter_classroom_links"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classes",
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
                ("class_name", models.CharField(max_length=200)),
                ("max_learner", models.IntegerField(default=0)),
                ("learners", models.CharField(max_length=300)),
                (
                    "educator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
