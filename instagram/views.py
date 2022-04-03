from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import json
from django.http import response
from django.shortcuts import render,redirect,get_object_or_404
from .models import Following, Image, Like,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.contrib.auth import login as dj_login

from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm,ImageForm,CommentForm
# Create your views here.

def say_hello(request):
    name='Instagram'
    return render(request,'index.html',{'name': name})

def registeruser(request):
    title = 'Register - instagram'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
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

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
    user = authenticate(request,username=username)
             
        