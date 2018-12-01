# Generated by Django 2.1.3 on 2018-12-01 00:03

from django.db import migrations, models


def delete_all_characters(apps, schema_editor):
    EveUser = apps.get_model('eve_auth', 'EveUser')
    EveUser.objects.all().delete()

    LogEntry = apps.get_model('admin', 'LogEntry')
    LogEntry.objects.all().delete()

def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('eve_auth', '0005_undo_custom_user_model'),
    ]

    operations = [
        migrations.RunPython(delete_all_characters, reverse_func),
    ]