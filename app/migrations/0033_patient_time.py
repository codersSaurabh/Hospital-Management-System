# Generated by Django 5.0.3 on 2024-05-11 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_remove_bill_day_spent_alter_bill_room_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Time',
            field=models.TimeField(default=datetime.time(16, 0)),
        ),
    ]
