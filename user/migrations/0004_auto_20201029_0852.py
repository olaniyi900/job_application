# Generated by Django 3.1.2 on 2020-10-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201029_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(default='maxwell', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(default='james', max_length=100),
            preserve_default=False,
        ),
    ]
