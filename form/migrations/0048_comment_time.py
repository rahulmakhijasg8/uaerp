# Generated by Django 3.2.9 on 2022-01-12 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0047_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
