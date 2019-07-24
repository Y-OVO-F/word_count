#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def yang(request):
    return  render(request,'yang.html')

def count(request):
    total_X = request.GET["x_text"]
    print(request.GET["y_text"])
    return  render(request,'count.html',{'count': total_X})