# Generated by Django 5.1.4 on 2025-01-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_userprofile_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='coins',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exp',
            field=models.IntegerField(default=5),
        ),
    ]
