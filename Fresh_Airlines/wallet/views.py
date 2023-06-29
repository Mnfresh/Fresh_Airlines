from django.shortcuts import render, redirect
from .models import Wallet
from .forms import BalanceAdditionForm, CurrencyForm


def wallet_view(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    balance = wallet.balance

    context = {
        'balance': balance,
        'currency': wallet.currency
    }

    return render(request, 'wallet/wallet.html', context)


def add_to_balance(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)

    if request.method == 'POST':
        form = BalanceAdditionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            wallet.balance += amount
            wallet.save()
            return redirect('wallet')

    else:
        form = BalanceAdditionForm()

    context = {
        'form': form,
    }

    return render(request, 'wallet/add_to_balance.html', context)


def change_currency(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    balance = wallet.balance
    currency = wallet.currency

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            conversion = form.cleaned_data['currency']
            if conversion == 'euro-to-leva':
                balance *= 1.96
                currency = 'BGN'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'leva-to-euro':
                balance *= 0.51
                currency = 'EUR'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'euro-to-pound':
                balance *= 0.86
                currency = 'GBP'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'pound-to-euro':
                balance /= 1.17
                currency = 'EUR'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'leva-to-pound':
                balance *= 0.44
                currency = 'GBP'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'pound-to-leva':
                balance *= 2.28
                currency = 'BGN'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'dollars-to-euro':
                balance *= 0.92
                currency = 'EUR'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'euro-to-dollars':
                balance *= 1.09
                currency = 'USD'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'dollars-to-leva':
                balance *= 1.79
                currency = 'BGN'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'leva-to-dollars':
                balance *= 0.56
                currency = 'USD'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'pound-to-dollars':
                balance *= 1.27
                currency = 'USD'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()
            elif conversion == 'dollars-to-pound':
                balance *= 0.79
                currency = 'GBP'
                wallet.balance = balance
                wallet.currency = currency
                wallet.save()

    else:
        form = CurrencyForm()

    context = {
        'balance': balance,
        'currency': currency,
        'form': form
    }

    return render(request, 'wallet/change_currency.html', context)

