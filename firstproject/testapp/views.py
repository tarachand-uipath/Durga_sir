from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
import datetime 

def hello_world(request):
 return HttpResponse('<h1>hello world </h1>')

# def hello_Tarachand(request):
#  return HttpResponse('<h1>hello Tarachand</h1>')

# def current_time(request):
#  date = datetime.datetime.now()
#  s=f'<h1> current time is {str(date)} <h1>'
#  return HttpResponse(s)

