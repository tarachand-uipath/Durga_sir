from ast import Delete
import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_response(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL+END_POINT ,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def get_response1():
    resp = requests.get(BASE_URL+END_POINT)
    print(resp.status_code)
    print(resp.json())

def create_resources():
    new_emp = {'eno':6431,
                'ename':'Rahul',
                'esalary':8000,
                'eadd':'Vashi'}

    resp = requests.post(BASE_URL+END_POINT , data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def update_resources(id=None):
    new_emp = {
        'id':id ,
        'esalary':9000,
                'eadd':'Mumbai'}

    resp = requests.put(BASE_URL+END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def delete_resources(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.delete(BASE_URL+END_POINT ,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())


delete_resources()