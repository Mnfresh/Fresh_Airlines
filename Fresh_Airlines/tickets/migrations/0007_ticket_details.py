# Generated by Django 4.2.2 on 2023-06-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_additional_baggage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
