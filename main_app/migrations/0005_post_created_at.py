# Generated by Django 5.2.3 on 2025-07-15 12:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_alter_comment_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
