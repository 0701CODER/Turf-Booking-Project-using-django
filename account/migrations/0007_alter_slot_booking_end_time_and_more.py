# Generated by Django 4.1.2 on 2022-11-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_user_otp_alter_slot_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_booking',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='slot_booking',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
