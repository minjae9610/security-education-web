# Generated by Django 4.1.2 on 2022-11-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_classes_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="classes",
            name="create_date",
            field=models.DateTimeField(null=True),
        ),
    ]