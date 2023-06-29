from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Fresh_Airlines.common.urls')),
    path('accounts/', include('Fresh_Airlines.accounts.urls')),
    path('tickets/', include('Fresh_Airlines.tickets.urls')),
    path('wallet/', include('Fresh_Airlines.wallet.urls')),
    path('weather/', include('Fresh_Airlines.weather.urls')),

]
