# Generated by Django 5.0.4 on 2024-05-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='confirm_password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
