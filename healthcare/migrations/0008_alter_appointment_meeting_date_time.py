<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-10-29 18:23
=======
# Generated by Django 4.2.6 on 2023-10-29 18:14
>>>>>>> 8f5427a5fd7e4e1cf39bb2bdc797c3ab4466628d

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0007_alter_appointment_meeting_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='meeting_Date_Time',
<<<<<<< HEAD
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 12, 53, 38, 937100, tzinfo=datetime.timezone.utc), verbose_name='Meeting Date and Time'),
=======
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 12, 44, 36, 346413, tzinfo=datetime.timezone.utc), verbose_name='Meeting Date and Time'),
>>>>>>> 8f5427a5fd7e4e1cf39bb2bdc797c3ab4466628d
        ),
    ]
