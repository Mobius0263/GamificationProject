# Generated by Django 5.1.4 on 2025-01-12 16:14

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_userprofile_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[50, 80], upload_to='profile_pics'),
        ),
    ]
