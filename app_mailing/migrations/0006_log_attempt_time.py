# Generated by Django 5.0 on 2024-01-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mailing', '0005_remove_log_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='attempt_time',
            field=models.DateTimeField(auto_now=True, verbose_name='время последней попытки'),
        ),
    ]