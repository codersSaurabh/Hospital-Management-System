# Generated by Django 5.0.3 on 2024-04-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_patient_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=30)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
