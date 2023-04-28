# Generated by Django 4.1.7 on 2023-04-28 04:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0012_user_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='classRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, max_length=254, null=True)),
                ('tutorsAccepted', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=1)),
                ('studentRequested', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=None)),
            ],
        ),
    ]
