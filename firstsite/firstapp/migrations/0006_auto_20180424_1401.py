# Generated by Django 2.0.3 on 2018-04-24 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comment', to='firstapp.Blog'),
        ),
    ]
