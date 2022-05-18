from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
    # print(dir(request))
    # request.body
    body = request.body # byte string of json b
    data = {}
    try: 
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers) # dict used casues json cannot prases this data directly
    data['content_type'] = request.content_type
    return JsonResponse(data)
