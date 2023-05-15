from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def show_peminjaman_stadium(request):
    context = {
    }
    return render(request, "peminjaman-stadium.html", context)

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def show_form_peminjaman_stadium(request):
    context = {
    }
    return render(request, "form-peminjaman-stadium.html", context)

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def show_list_waktu_stadium(request):
    context = {
    }
    return render(request, "list-waktu-stadium.html", context)
