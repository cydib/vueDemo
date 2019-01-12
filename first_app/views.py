import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def get_array(request):
    ret = [1, 2, 3, 4, 5, 6]
    return JsonResponse(ret, safe=False)


data = ["apple", "orange", "banana", "pear", "juice"]


def search(request):
    if "POST" == request.method:
        body = json.loads(request.body)
        print(body)
        if "key" not in body:
            return JsonResponse([], safe=False)
        key = body["key"]
        print(key)
        ret = []
        for i in data:
            if key in i:
                ret.append(i)
        return JsonResponse(ret, safe=False)

    else:
        return HttpResponse(status=404)
