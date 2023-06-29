from django.urls import path
from . import views
from .views import add_to_balance, change_currency

urlpatterns = [
    path('wallet/', views.wallet_view, name='wallet'),
    path('add-to-balance/', add_to_balance, name='add_to_balance'),
    path('change-currency/', change_currency, name='change_currency'),
]
