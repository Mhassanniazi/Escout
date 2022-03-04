from django.shortcuts import render,redirect
from django.http import HttpResponse
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import json
# Create your views here.
def dashboard(request):
    # if request.method=="POST":
    #     # print(request.POST.dict())
    #     new=request.POST.dict()
    #     new=list(new.items())
    #     print(list(new))
    #     urlss=new[1][1]
    #     options=Options()
    #     options.headless=True
    #     driver = webdriver.Chrome('E:\DJ\ESCOUT\chromedriver.exe',options=options)
    #     driver.get(urlss)

    #     name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
    #     price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
    #     shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
    #     print(name,"--",price,"--",shopname)
        ## seeling price,rating,storename,name,

    context={}
    return render(request,"PHT/dashboard.html",context)
def addproduct(request):
    context={}
    return render(request,"PHT/addproduct.html",context)

def profitcalculator(request):
    context={}
    return render(request,"PHT/profit.html",context)

def index(request):
    return render(request,'PHT/index.html')