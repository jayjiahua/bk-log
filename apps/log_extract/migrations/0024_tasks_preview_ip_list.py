# Generated by Django 3.2.15 on 2023-03-27 03:55

import apps.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("log_extract", "0023_auto_20210705_1729"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasks",
            name="preview_ip_list",
            field=apps.models.JsonField(blank=True, null=True, verbose_name="预览地址ip列表"),
        ),
    ]
