from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def show_list_pertandingan(request):
    context = {
    }
    return render(request, "list-pertandingan.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_pembuatan_pertandingan(request):
    context = {
    }
    return render(request, "pembuatan-pertandingan.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_form_pembuatan_pertandingan(request):
    context = {
    }
    return render(request, "form-pembuatan-pertandingan.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_form_pemilihan_jadwal(request):
    context = {
    }
    return render(request, "form-pemilihan-jadwal.html", context)