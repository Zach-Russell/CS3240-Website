# Generated by Django 4.1.7 on 2023-05-02 03:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0014_classrequest_tutorsalreadyaccepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrequest',
            name='tutorsAlreadyAccepted',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=None),
        ),
    ]
