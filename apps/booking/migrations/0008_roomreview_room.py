# Generated by Django 4.2.2 on 2023-07-05 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_room_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreview',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.room'),
        ),
    ]
