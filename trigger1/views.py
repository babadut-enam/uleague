from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user) # melakukan login terlebih dahulu
                response = HttpResponseRedirect(reverse("trigger1:dashboard")) # membuat response
                response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
                return response
            else:
                messages.info(request, 'Username atau Password salah!')
        else:
            messages.error(request, 'Form tidak valid')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('trigger1:login'))
    response.delete_cookie('last_login')
    return response

def register(request):
    context = {
    }
    return render(request, "register/register.html", context)

def register_panitia(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('trigger1:login')
        else:
            messages.error(request, 'Form tidak valid')
    
    context = {'form': form}
    return render(request, 'register/register-panitia.html', context)

def register_manajer_penonton(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('trigger1:login')
        else:
            messages.error(request, 'Form tidak valid')

    context = {'form': form}
    return render(request, 'register/register-manajer-penonton.html', context)

def show_home(request):
    context = {
    }
    return render(request, "home.html", context)

@csrf_exempt
#@login_required(login_url='/trigger1/login/')
def show_dashboard(request):
    context = {
    }
    return render(request, "dashboard/dashboard.html", context)

@csrf_exempt
#@login_required(login_url='/trigger1/login/')
def show_dashboard_manajer(request):
    context = {
    }
    return render(request, "dashboard/dashboard-manajer.html", context)