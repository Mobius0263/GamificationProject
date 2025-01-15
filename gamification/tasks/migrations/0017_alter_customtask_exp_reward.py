# Generated by Django 5.1.4 on 2025-01-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_customtask_exp_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtask',
            name='exp_reward',
            field=models.IntegerField(default=0, verbose_name=[(50, '50 EXP'), (75, '75 EXP'), (100, '100 EXP')]),
        ),
    ]
