# Generated by Django 4.2.2 on 2023-06-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticket_place_in_plane'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='additional_baggage',
            field=models.BooleanField(default=False),
        ),
    ]