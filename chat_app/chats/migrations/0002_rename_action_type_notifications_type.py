# Generated by Django 4.0.5 on 2022-06-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='action_type',
            new_name='type',
        ),
    ]
