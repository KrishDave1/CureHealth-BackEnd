# Generated by Django 4.2.6 on 2023-10-29 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0009_alter_appointment_meeting_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='meeting_Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 13, 48, 51, 611401, tzinfo=datetime.timezone.utc), verbose_name='Meeting Date and Time'),
        ),
    ]
