# Generated by Django 3.2.9 on 2021-12-23 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0026_hotelinfo_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelinfo',
            name='Payments',
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='Hpaymentskey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.hotelinfo'),
        ),
    ]
