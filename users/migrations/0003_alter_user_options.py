# Generated by Django 4.2.7 on 2024-01-19 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('pk',), 'permissions': [('set_is_activated', 'переключатель метки активности')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
