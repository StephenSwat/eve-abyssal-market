# Generated by Django 2.1.3 on 2018-12-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abyssal_modules', '0015_rename_new_attribute'),
        ('eve_auth', '0009_evedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownership_records', to='abyssal_modules.Module')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_records', to='eve_auth.EveUser')),
            ],
        ),
    ]