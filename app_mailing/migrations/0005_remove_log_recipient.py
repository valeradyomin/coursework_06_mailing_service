# Generated by Django 5.0 on 2024-01-07 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mailing', '0004_rename_attempt_status_log_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='recipient',
        ),
    ]