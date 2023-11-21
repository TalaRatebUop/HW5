from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
RoomNumber=[2233,4566,222,56,22224]
def index2(request):
    return render(request,"info.html",{"RoomNumber":RoomNumber})