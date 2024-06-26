# Generated by Django 5.0.3 on 2024-04-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_doctor_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_id', models.CharField(default='', max_length=10)),
                ('Room_charges', models.IntegerField(default=0)),
                ('Doctor_charges', models.IntegerField(default=0)),
                ('Medicine_charges', models.IntegerField(default=0)),
                ('Other_charges', models.IntegerField(default=0)),
            ],
        ),
    ]
