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
        
        user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect(reverse('welcome'))
    else:
        messages.info(request,'Username or password is incorrect')
        
        
        context={}
        return render(request,'login.html',context)
    
    
    @login_required(login_url='login')
    def logout(request):
        
        return redirect(reverse('login'))
    @login_required(login_url='login')
    def welcome(request):
        photo=Image.object.all()
        user=request.user
        
        context ={'photos':photos,'user':user}
        return render (REQUEST,'welcome.html',context)
        
    @login_required
    def profile(request):
        if request.methof == 'POST':
            u_form = UpdateprofileForm(request.POST,instance=request.user)
            p_form = UpdateprofileForm(request.POST,request.FILES,instance=request.user.profile)
           
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            
            return render(request, 'profile.html', context)
        
                
def search_results(request):
    if 'photo' in  request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_profiles = Profile.search_profile(search_term)
        message = f'{search_term}'   
        
        return render(request, 'search.html', {'message':message,'photos': searched_profiles})    
             
        