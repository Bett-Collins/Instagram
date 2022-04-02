from django.urls import path
from . import views

#urlConf
urlpatterns =[
   path('',views.say_hello, name='index') 
]