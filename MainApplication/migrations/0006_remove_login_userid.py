# Generated by Django 2.0.3 on 2018-10-04 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0005_auto_20181004_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='userId',
        ),
    ]