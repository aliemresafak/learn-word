# Generated by Django 4.1 on 2022-08-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0003_category_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
