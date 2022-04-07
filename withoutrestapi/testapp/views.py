from dataclasses import fields
from distutils.log import error
from email.mime import nonmultipart
from logging.config import fileConfig
from turtle import update
from wsgiref import validate
from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin
from testapp.mixins import HttpResponseMixin
from testapp.utils import is_json
from testapp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt , name = 'dispatch')
class EmployeeDetailsCBV(HttpResponseMixin,SerializeMixin,View):

    def get_object_by_id(self ,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp


    def get(self , resquest , id ,*args ,**kwargs):
        try:
            
            emp = Employee.objects.get(id=id)
            
        except Employee.DoesNotExist:
            print('yes')
            emp_json = json.dumps({'msg':'Resources does not available'})
        # emp_data = {
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esalary':emp.esalary,
        #     'eadd':emp.eadd
        # }

        # emp_json =  json.dumps(emp_data)
        else:
            emp_json = serialize('json' , [emp,])
            p_data  = json.loads(emp_json)
            final_list = [i['fields'] for i in p_data]
            emp_json = json.dumps(final_list)
        return HttpResponse(emp_json , content_type = 'application/json')

    def put(self , resquest , id ,*args ,**kwargs):
        # emp = self.get_object_by_id(id)
        # if emp is None:
        #     json_data = json.dumps({'msg':'Record does not exits'})
        #     return self.render_http_response(json_data , status=400)
        data =  resquest.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid json data'})
            return self.render_http_response(json_data , status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Record does not exits'})
            return self.render_http_response(json_data , status=400)
        provided_data= json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esalary':emp.esalary,
            'eadd':emp.eadd
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data , instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data =  json.dumps({'msg':'Resources updated successfully'})
            return self.render_http_response(json_data)
        if form.errors:
            json_data =  json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)

    def delete(self,request,id,*args,**kwargs):
        emp =  self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Record does not exits for deletion'})
            return self.render_http_response(json_data , status=400)
        status , deleted_item = emp.delete()
        if status == 1:
            json_data =  json.dumps({'msg':'Resources deleted successfully'})
            return self.render_http_response(json_data)
        json_data =  json.dumps({'msg':'Unable to delete the resource plz try again'})
        return self.render_http_response(json_data)
        



@method_decorator(csrf_exempt , name = 'dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self , resquest ,*args ,**kwargs):
        emp = Employee.objects.all()
        # emp_data = {
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esalary':emp.esalary,
        #     'eadd':emp.eadd
        # }

        # emp_json =  json.dumps(emp_data)
        # emp_json = serialize('json' ,emp)
        # p_data  = json.loads(emp_json)
        # # final_list = [i['fields'] for i in p_data]
        # final_list = []
        # for obj in p_data:
        #     final_list.append(obj['fields'])
        # emp_json = json.dumps(final_list)



        

        return HttpResponse(self.serialize(emp) , content_type = 'application/json')



    def post(self , request , *args , **kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid data'})
            return self.render_http_response(json_data , status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data =  json.dumps({'msg':'Resources created successfully'})
            return self.render_http_response(json_data)
        if form.errors:
            json_data =  json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)


@method_decorator(csrf_exempt , name = 'dispatch')
class EmployeeCURDCVB(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self ,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp


    def get(self ,request , *args , **kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid data'})
            return self.render_http_response(json_data , status=400)
        pdata = json.loads(data)
        id = pdata.get('id' , None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'Requested resource Not available with given Id'})
                return self.render_http_response(json_data , status=400)
            json_data = self.serialize([emp ,])
            return self.render_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_http_response(json_data)


    def post(self , request , *args , **kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid data'})
            return self.render_http_response(json_data , status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data =  json.dumps({'msg':'Resources created successfully'})
            return self.render_http_response(json_data)
        if form.errors:
            json_data =  json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)

    def put(self ,request , *args , **kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid data'})
            return self.render_http_response(json_data , status=400)
        pdata = json.loads(data) 
        id =  pdata.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'For Updation please send Id'})
            return self.render_http_response(json_data , status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Requested resource Not available for updation'})
            return self.render_http_response(json_data , status=400)

        provided_data= json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esalary':emp.esalary,
            'eadd':emp.eadd
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data , instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data =  json.dumps({'msg':'Resources updated successfully'})
            return self.render_http_response(json_data)
        if form.errors:
            json_data =  json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)

    def delete(self ,request , *args , **kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg':'Not a valid data'})
            return self.render_http_response(json_data , status=400)
        pdata = json.loads(data)
        id = pdata.get('id' , None)
        if id is not None:
            emp = self.get_object_by_id(id)
    
            if emp is None:
                json_data = json.dumps({'msg':'Requested resource Not available with given Id'})
                return self.render_http_response(json_data , status=400)
            status , deleted_item = emp.delete()
            if status == 1:
                json_data =  json.dumps({'msg':'Resources deleted successfully'})
                return self.render_http_response(json_data)
            json_data =  json.dumps({'msg':'Unable to delete the resource plz try again'})
            return self.render_http_response(json_data)
        json_data = json.dumps({'msg':'For Deletion please send Id'})
        return self.render_http_response(json_data , status=400)
        



                
