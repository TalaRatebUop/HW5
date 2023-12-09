from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django import forms
# Create your views here.
RoomNumber=[2233,4566,222,56,22224]
def index2(request):
    return render(request,"info.html",{"RoomNumber":RoomNumber})
def add(request):
    return render(request,"add.html")

products=[]
class product(forms.Form):
    CATEGORY=[(1,"Food"),(2,"Snacks"),(3,"Drinks"),(4,"Hardware")]
    productName=forms.CharField(label="Product Name",label_suffix=":")
    Category=forms.ChoiceField(label="Category",label_suffix=":",choices=CATEGORY)
    description=forms.CharField(label="Description ",label_suffix=":")
    rate=forms.DecimalField(label="Rate",label_suffix=":")
def info2(request):
    if 'no_product' not in request.session:
        request.session['no_product'] = 0
    return render(request,"info2.html",{"products":list(enumerate(products)),"Noproduct":request.session['no_product']})
def add2(request):
    if request.method == 'POST':
        b=product(request.POST)
        if b.is_valid():
            products.append(request.POST)
            if 'no_product' not in request.session:
                request.session['no_product']=0
            request.session['no_product'] += 1
            return redirect(reverse("info2"))
        else:
            return render(request, "add2.html", {"form": b})
    b2 = product()
    return render(request, "add2.html", {"form":b2})