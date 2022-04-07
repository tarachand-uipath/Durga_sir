from django.shortcuts import render
from django.http import HttpResponse

def good_morning(request):
 return HttpResponse('<h1>Good Morning</h1>')