# Generated by Django 4.1.7 on 2023-03-29 01:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_schedule_tutortimings'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='tutorRequests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default='{}', size=None),
        ),
    ]
