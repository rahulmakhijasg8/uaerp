# Generated by Django 3.2.9 on 2022-01-14 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0052_alter_comment_bookingkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
