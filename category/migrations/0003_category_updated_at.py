# Generated by Django 4.1 on 2022-08-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0002_category_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="updated_at",
            field=models.DateField(auto_now=True),
        ),
    ]