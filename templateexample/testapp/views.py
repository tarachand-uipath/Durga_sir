from django.shortcuts import render 
from django.http import HttpResponse
import datetime


def view(request):
 date = datetime.datetime.now()
 hour = int(date.strftime('%H'))
 # hour = 22


 msg = 'Hello Tarachand'
 if hour < 12:
  msg = msg + ' Good Morning '
 elif hour < 16 :
  msg = msg + ' Good Afternoon'
 elif hour < 21 :
  msg = msg + ' Good Evening'
 else:
  msg = msg + ' Good Night'
 return render(request , 'testapp/result.html' , {'m':msg,'date':date})

def view2(request):
 return render(request , 'testapp/result1.html') 
