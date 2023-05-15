from django.urls import path
from trigger6.views import pembelian_tiket, pembelian_tiket2, pembelian_tiket3, pembelian_tiket4

app_name = 'trigger6'

urlpatterns = [
    path('pembelian-tiket-stadium/', pembelian_tiket, name='pembelian_tiket'),
    path('pembelian-tiket-waktu/', pembelian_tiket2, name='pembelian_tiket2'),
    path('pembelian-tiket-vs/', pembelian_tiket3, name='pembelian_tiket3'),
    path('pembelian-tiket-checkout/', pembelian_tiket4, name='pembelian_tiket4'),
]