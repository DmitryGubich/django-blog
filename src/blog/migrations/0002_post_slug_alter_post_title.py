# Generated by Django 4.2.7 on 2023-11-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="default", unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]