# Generated by Django 5.1.4 on 2025-01-13 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_task_last_reset_alter_task_user_usertaskcompletion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
