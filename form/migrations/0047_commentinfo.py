# Generated by Django 3.2.9 on 2022-01-14 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0046_alter_bookinginfo_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_Type', models.CharField(max_length=255)),
                ('duedate', models.DateField(default=datetime.date.today)),
                ('Comment', models.TextField()),
                ('User', models.CharField(max_length=255)),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Tag', models.CharField(max_length=255)),
                ('Acpaymentskey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acp', to='form.activitiesinfo')),
                ('Bookingkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bp', to='form.bookinginfo')),
                ('Hopaymentskey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hop', to='form.hotelinfo')),
                ('Ticpaymentskey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticp', to='form.ticketinfo')),
                ('Trpaymentskey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trp', to='form.transportinfo')),
            ],
        ),
    ]
