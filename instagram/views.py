from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    name='Instagram'
    return render(request,'index.html',{'name': name})
