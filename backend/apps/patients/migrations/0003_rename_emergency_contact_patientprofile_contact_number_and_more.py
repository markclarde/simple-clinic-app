# Generated by Django 5.2.4 on 2025-07-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_remove_patientprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='emergency_contact',
            new_name='contact_number',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
