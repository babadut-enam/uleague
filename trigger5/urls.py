from django.urls import path
from trigger5.views import show_manage_pertandingan, show_peristiwa_tim, mulai_pertandingan, tim1_peristiwa, tim2_peristiwa
from trigger5.views import show_history_rapat, form_isi_rapat, mulai_rapat

app_name = 'trigger5'

urlpatterns = [
    path('manage-pertandingan/', show_manage_pertandingan, name='manage-pertandingan'),
    path('manage-pertandingan/peristiwa-tim/', show_peristiwa_tim, name='peristiwa-tim'),
    path('mulai-pertandingan/', mulai_pertandingan, name='mulai_pertandingan'),
    path('tim1-peristiwa/', tim1_peristiwa, name='tim1_peristiwa'),
    path('tim2-peristiwa/', tim2_peristiwa, name='tim2_peristiwa'),
    path('history-rapat/', show_history_rapat, name='history-rapat'),
    path('form-isi-rapat/', form_isi_rapat, name='form_isi_rapat'),
    path('mulai-rapat/', mulai_rapat, name='mulai_rapat'),
]