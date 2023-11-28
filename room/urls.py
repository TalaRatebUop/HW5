from  django.urls import path
from . import  views
urlpatterns=[
    path("",views.index2),
    path('add',views.add, name="add"),
    path("product1",views.product1,name="product1"),
    path('addP',views.addProduct,name="addP")
             ]