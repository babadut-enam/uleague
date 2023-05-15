from django.urls import path
from trigger1.views import login_user, logout_user
from trigger1.views import register, register_manajer_penonton, register_panitia
from trigger1.views import show_home, show_dashboard, show_dashboard_manajer

app_name = 'trigger1'

urlpatterns = [
    path('', show_home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('register-manajer-penonton/', register_manajer_penonton, name='register-manajer-penonton'),
    path('register-panitia/', register_panitia, name='register-panitia'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('dashboard-manajer/', show_dashboard_manajer, name='dashboard-manajer'),
]