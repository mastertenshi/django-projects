from django.urls import path

from .views import OrdersView, charge

app_name = 'orders'

urlpatterns = [
    path('', OrdersView.as_view(), name='order'),
    path('charge/', charge, name='charge'),
]
