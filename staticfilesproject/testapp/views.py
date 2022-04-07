import imp
from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
 my_dict = {'name':'Tarachand','Add':'chembur','Work':'developer'}
 return render(request , 'testapp/result.html',my_dict)

def view2(request):
 return render(request , 'testapp/result1.html')

