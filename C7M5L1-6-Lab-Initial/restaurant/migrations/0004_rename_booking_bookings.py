# Generated by Django 5.1 on 2025-05-18 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Bookings',
        ),
    ]
