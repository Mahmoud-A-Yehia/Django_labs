from django.shortcuts import render
# from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    return render(request=request,template_name="home.html")


# @api_view(['GET','POST'])
def track(request):
    if request.method == 'GET':
        with open("../orders.xlsx","r") as file:
            orders=file.read()
        return orders

        
