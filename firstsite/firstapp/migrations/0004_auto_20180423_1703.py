# Generated by Django 2.0.3 on 2018-04-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20180421_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='comment',
            new_name='content',
        ),
    ]
