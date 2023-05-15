from django.urls import path
from trigger3.views import show_peminjaman_stadium, show_form_peminjaman_stadium, show_list_waktu_stadium

app_name = 'trigger3'

urlpatterns = [
    path('peminjaman-stadium/', show_peminjaman_stadium, name='peminjaman-stadium'),
    path('form-peminjaman-stadium/', show_form_peminjaman_stadium, name='form-peminjaman-stadium'),
    path('waktu-stadium/', show_list_waktu_stadium, name='waktu-stadium'),
]