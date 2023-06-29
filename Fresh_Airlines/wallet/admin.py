from django.contrib import admin
from Fresh_Airlines.wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'currency']
