# Generated by Django 5.1.4 on 2025-01-13 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userachievement',
            name='achievement',
        ),
        migrations.RemoveField(
            model_name='dailytask',
            name='task',
        ),
        migrations.RemoveField(
            model_name='dailytask',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useritem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='userachievement',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useritem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='coin_reward',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_custom',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='coins',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 1, 13, 19, 8, 36, 178800, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Achievement',
        ),
        migrations.DeleteModel(
            name='DailyTask',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='UserAchievement',
        ),
        migrations.DeleteModel(
            name='UserItem',
        ),
    ]
