# Generated by Django 3.2.9 on 2022-01-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0047_commentinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='Bookingkey',
            field=models.CharField(default='', max_length=255),
        ),
    ]
