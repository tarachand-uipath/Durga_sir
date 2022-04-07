from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializeMixin(object):
    def serialize(self,qs):
        emp_json = serialize('json' ,qs)
        p_data  = json.loads(emp_json)
        final_list = []
        for obj in p_data:
            final_list.append(obj['fields'])
        emp_json = json.dumps(final_list)
        return emp_json

class HttpResponseMixin(object):
    def render_http_response(self,json_data , status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)

    
