from django.contrib import admin

from Fresh_Airlines.tickets.models import Ticket


@admin.register(Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ["start_country", 'end_country', 'start_city', 'end_city', 'start_airport', 'end_airport', "price",
                    "currency"]
