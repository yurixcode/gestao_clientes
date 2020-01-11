from django.shortcuts import render, redirect
from django.contrib.auth import logout

# TODO: Hacer seguimiento de solicitudes
def home(request):
    return render(request, 'home.html')

# FIXME: No funka nene
def my_logout(request):
    logout(request)
    return redirect('home')
