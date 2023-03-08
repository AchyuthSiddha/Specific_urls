from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Virat(request):
    return HttpResponse("<h1><mark>Virat is best batsman in world</h1>")
def ABD(request):
    return HttpResponse("<h1><marquee>ABD is mr 360</marquee></h1>")
