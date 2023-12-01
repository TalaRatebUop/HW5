from  django.urls import path
from . import  views
urlpatterns=[
    path("",views.index2),
    path('add',views.add, name="add"),
    path('add2',views.add2, name="add2"),
    path('info2',views.info2, name="info2"),
             ]