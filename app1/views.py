from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Dhoni(request):
    return HttpResponse("<h1><marquee>Dhoni is Best Finisher in india</marquee></h1>")
def Raina(request):
    return HttpResponse("<h1><mark>Raina is Mr.IPL</h1>")
