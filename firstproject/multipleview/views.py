from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
 return HttpResponse('<h1>First view</h1>')

def second_view(request):
 return HttpResponse('<h1>Second view</h1>')

def third_view(request):
 return HttpResponse('<h1>Third view</h1>')

def forth_view(request):
 return HttpResponse('<h1>Forth view</h1>')