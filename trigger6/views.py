from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def pembelian_tiket(request):
  user = request.user
  context = {
    }
  return render(request, "pembelian-tiket.html", context)

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def pembelian_tiket2(request):
  user = request.user
  context = {
    }
  return render(request, "pembelian-tiket2.html", context)

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def pembelian_tiket3(request):
  user = request.user
  context = {
    }
  return render(request, "pembelian-tiket3.html", context)

@csrf_exempt
#@login_required(login_url='/sepakbola/login/')
def pembelian_tiket4(request):
  user = request.user
  context = {
    }
  return render(request, "pembelian-tiket4.html", context)
