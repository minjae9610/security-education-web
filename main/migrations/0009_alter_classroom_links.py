# Generated by Django 4.1.2 on 2022-10-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_classroom_links"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classroom",
            name="links",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
