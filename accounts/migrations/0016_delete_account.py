# Generated by Django 5.0.2 on 2024-06-22 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_account_groups_and_more'),
        ('admin', '0004_alter_logentry_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
