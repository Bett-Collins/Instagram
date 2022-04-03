from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django import forms
from .models import Following, Image, Like,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.http import response
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

def say_hello(request):
    name='Instagram'
    return render(request,'index.html',{'name': name})

def registeruser(request):
    title = 'Register - instagram'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid()
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')
            
            return redirect('login')
    else:
        form = CreateUserForm
    context = {
        'title':title,
        'form':form,
    }   
    
    return render(request, 'register.html',context) 
             
        