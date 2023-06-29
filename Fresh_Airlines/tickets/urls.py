from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.ticket_list, name='tickets'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('buy_ticket/<int:pk>', views.buy_ticket, name='buy_ticket')
]
