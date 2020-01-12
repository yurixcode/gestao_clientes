from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View


# TODO: Hacer seguimiento de solicitudes
def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')


class MyView(View):
    def get(self, request, *args, **kwargs):
       return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

