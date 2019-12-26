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

def index(request):
    return HttpResponse("<h2>Main page</h2>")


def about(request):
    return HttpResponse("<h2>About</h2>")


def contact(request):
    return HttpResponse("<h2>Contacts</h2>")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product # {0} Category {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    user_id = request.GET.get("user_id", 1)
    name = request.GET.get("name", "USERNAME")
    output = "<h2>User</h2><h3>id: {0} name : {1}</h3>".format(user_id, name)
    return HttpResponse(output)
