# Generated by Django 5.0.2 on 2024-07-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_exercises_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineraccount',
            name='city',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
