from django.urls import path
from django.db.models.query import ValuesIterable

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('uploadImage/',views.uploadImage,name = 'uploadImage'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('search/', views.search_results, name='search_results'),
    path('like/', views.like, name='like'),
    path('photo/<str:pk>',views.viewPhoto,name='photo'),
    path('follow/<str:username>',views.follow,name='follow'),
    path('post/<int:pk>/comment', views.post_detail, name='post_detail'),
    

]
