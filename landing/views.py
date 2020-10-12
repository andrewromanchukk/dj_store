from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    name = 'Andrew'
    return render(request, 'landing/landing.html', locals())
