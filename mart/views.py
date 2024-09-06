from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    varname=[{"name":"book" , "price":22},{"name":"laptop" , "price":220},{"name":"game" , "price":100}]
    # varname={"name":"book" , "price":22}
    # varname="ahmed"
    return render(request,"mart/index.html",{"products":varname})