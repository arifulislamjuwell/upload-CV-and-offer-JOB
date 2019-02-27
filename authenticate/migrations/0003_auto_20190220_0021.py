# Generated by Django 2.0.13 on 2019-02-19 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(default=datetime.datetime(2019, 2, 19, 18, 20, 24, 187253, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=datetime.datetime(2019, 2, 19, 18, 21, 11, 43784, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=datetime.datetime(2019, 2, 19, 18, 21, 44, 827139, tzinfo=utc), upload_to='uploads/profile/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]