from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from . import Form
# Create your views here.
RoomNumber=[2233,4566,222,56,22224]
def index2(request):
    return render(request,"info.html",{"RoomNumber":RoomNumber})
def add(request):
    return render(request,"add.html")
def product1(request):
    return render(request,"product.html",{"product":product})
product=[]
def addProduct(request):
     if request.method=="POST":
         p = Form.product(request.POST)

         if p.is_valid():
            product.append(request.POST)
            return render(request,"product.html")

     else :
         p2=Form.product(request.POST)
         return render(request,"addProduct.html",{"form":p2})