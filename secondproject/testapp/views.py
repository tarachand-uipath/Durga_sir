import imp
from django.shortcuts import render
import datetime

def template_view(request):
 date = datetime.datetime.now()
 my_dict = {'date':date, 'name':'Tarachand'}
 return render(request , 'testapp/result.html' , context=my_dict)
