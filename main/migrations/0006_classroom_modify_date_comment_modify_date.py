# Generated by Django 4.1.2 on 2022-10-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_auto_20221019_0503"),
    ]

    operations = [
        migrations.AddField(
            model_name="classroom",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
