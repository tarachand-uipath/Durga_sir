import imp
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from testapp.mixins import HttpResponseMixin

def emp_data_view(request):
 emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000
 }

 resp = f'<h1>Employee Name {emp["ename"]} ,Employee work {emp["ework"]} ,Employee add {emp["eadd"]} ,Employee salary {emp["esalary"]} </h1>'

 return HttpResponse(resp)

import json
def emp_data_json_view(request):
 emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000
 }
 json_data = json.dumps(emp)
 
 return HttpResponse(json_data , content_type='application/json')

from django.http import JsonResponse
def emp_data_json_view2(request):
 emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000 ,
  'skills' : ['Python' 'HTML' ,'CSS','Javascripts','Reactjs']
 }
 
 
 return JsonResponse(emp)


from django.views.generic import View

class JsonCBV(View):

 def get(self , request , *args ,**kwargs):
  emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000 ,
  'skills' : ['Python' 'HTML' ,'CSS','Javascripts','Reactjs']
 }
 
 
  return JsonResponse(emp)

 def post(self , request , *args ,**kwargs):
  emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000 ,
  'skills' : ['Python' 'HTML' ,'CSS','Javascripts','Reactjs']
 }
 
 
  return JsonResponse(emp)

 def delete(self , request , *args ,**kwargs):
  emp = {
  'ename':'Tarachand',
  'ework':'Developer',
  'eadd' : 'chembur',
  'esalary' : 5000 ,
  'skills' : ['Python' 'HTML' ,'CSS','Javascripts','Reactjs']
 }
 
 
  return self.render_to_httpresponse(emp)


