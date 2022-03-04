from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('profitcalculator/',views.profitcalculator,name='profitcalculator'),
]