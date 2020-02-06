from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View


# TODO: Hacer seguimiento de solicitudes
def home(request):
    return render(request, 'home/home.html')

def my_logout(request):
    logout(request)
    return redirect('home')


class MyView(View):
    def get(self, request, *args, **kwargs):


       response = render_to_response('home3.html')
       response.set_cookie('color', 'azul', max_age=1000)

       mycookie = request.COOKIES.get('color')
       return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

