from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def get_array(request):
    ret = [1, 2, 3, 4, 5, 6]
    return JsonResponse(ret, safe=False)
