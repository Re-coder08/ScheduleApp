# Generated by Django 4.2.7 on 2023-11-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='staff_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='staff_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
