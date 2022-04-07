from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def employee_view(request):
 employees = Employee.objects.all()
 return  render(request , 'testapp/result.html' ,{"employee":employees})