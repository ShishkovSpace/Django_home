from typing import Dict, Union

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def homepage(request):
    header = "Homepage"
    user = {'name': "Alex", 'age': 26}
    message = "Tomorrow you will suffer! Because you are already "
    data = {"header": header, "message": message, "user": user}
    return render(request, "homepage.html", context=data)

def firstpage(request):
    message = "With Template response"
    data = {"message": message}
    return TemplateResponse(request, "firstpage.html", data)