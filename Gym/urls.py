from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect



urlpatterns = [
   
   path('',views.home,name="Home"),
   path('admin/', admin.site.urls),
   
   path('signup/', views.signup, name='signup'),
   path('login/',views.handlelogin,name="handlelogin"),
   path('logout/',views.handleLogout,name="handlelogout"),
   path('dashboard/', dashboard, name='dashboard'),
   path('password_change_form/', auth_views.PasswordChangeView.as_view(), name ='password_change_form'),
   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name ='password_change_done'),
   path('predict/',views.predict, name= 'predict'),



   
]

