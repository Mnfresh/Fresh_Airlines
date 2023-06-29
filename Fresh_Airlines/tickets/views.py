from django.shortcuts import render, redirect
from .models import Ticket, PurchasedTicket
from ..wallet.models import Wallet



def ticket_list(request):
    purchased_tickets = PurchasedTicket.objects.filter(user=request.user).values_list('ticket', flat=True)
    tickets = Ticket.objects.exclude(id__in=purchased_tickets)
    return render(request, 'ticket/tickets.html', {'tickets': tickets})


def my_tickets(request):
    mytickets = PurchasedTicket.objects.filter(user=request.user)
    return render(request, 'ticket/my_tickets.html', {'mytickets': mytickets})


def buy_ticket(request, pk):
    user_wallet = Wallet.objects.get(user=request.user)
    my_balance = user_wallet.balance
    current_currency = user_wallet.currency
    ticket = Ticket.objects.get(id=pk)

    if ticket:
        if my_balance >= ticket.price and ticket.currency == current_currency:
            my_ticket = PurchasedTicket(user=request.user, ticket=ticket)
            my_ticket.save()

            my_balance -= ticket.price
            user_wallet.balance = my_balance
            user_wallet.save()

            return redirect('my_tickets')

    return redirect('tickets')
