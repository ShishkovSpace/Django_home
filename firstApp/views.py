from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
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
