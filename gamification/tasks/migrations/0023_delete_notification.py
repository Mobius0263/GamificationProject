# Generated by Django 5.1.4 on 2025-01-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_alter_customtask_exp_reward'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
