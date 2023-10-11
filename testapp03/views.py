from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def good_morning_view(request):  
    return HttpResponse('<h1>Hello Friend,Good morning<h1>')

def good_evening_view(request):
    return HttpResponse('<h1>Hello Friend,Good evening!!<h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1>Hello Friend,Good afternoon<h1>')