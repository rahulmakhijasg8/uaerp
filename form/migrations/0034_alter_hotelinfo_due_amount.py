# Generated by Django 3.2.9 on 2021-12-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0033_alter_hotelinfo_due_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelinfo',
            name='Due_Amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]