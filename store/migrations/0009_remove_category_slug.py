# Generated by Django 5.1.5 on 2025-03-03 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
