import contextlib
from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .import forms
from .forms import NotificationForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Member
from django.contrib.auth import login, logout, authenticate
import pandas as pd
from .forms import PredictionForm  
import os
import joblib
from . import views




def home(request):
    return render(request, "index.html")

def signup(request):
       
    if request.method != "POST":
      return render(request,"signup.html")
    
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username=request.POST.get('usernumber')
    email=request.POST.get('email')
    pass1=request.POST.get('pass1')
    pass2=request.POST.get('pass2')

    if len(username)>11 or len(username)<11:
        messages.info(request,"Phone Number Must be 11 Digits")
        return redirect('/signup')

    
    if len(pass1) < 10:
        messages.info(request, "Password Length Requirements atleast 10")
        return redirect('/signup')

    if pass1 != pass2:
        messages.info(request, "Password is not Matching")
        return redirect('/signup')

   
   
    with contextlib.suppress(Exception):
        if User.objects.get(username=username):
            messages.warning(request,"Phone Number is Taken")
            return redirect('/signup')

    with contextlib.suppress(Exception):
        if User.objects.get(email=email):
            messages.warning(request,"Email is Taken")
            return redirect('/signup')

    myuser=User.objects.create_user(username,email,pass1)
    myuser.first_name = first_name
    myuser.last_name = last_name
    myuser.save()
    messages.success(request,"User is Created Please Login")
    return redirect('/login')
   
 

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')

        myuser=authenticate(username=username,password=pass1)
        
        if myuser is not None:

            login(request, myuser)
            messages.success(request,"Login Successful")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')




def home(request):
    msg = ''
    form = forms.NotificationForm()

    if request.method == 'POST':
        form = forms.NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Enquiry has been sent!'

            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']  # Corrected field name
            message = form.cleaned_data['message']

            send_mail(
                'Contact Form Submission',
                f'Name: {name,}\nMessage: {message}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
           
            form = forms.NotificationForm()  # Reset the form after successful submission
        else:
            msg = 'There was an error in your submission. Please try again.'

    return render(request, 'index.html', {'form': form, 'msg': msg})



def dashboard(request):
   
    return render(request, 'dashboard.html')





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'static', 'calories_model.pkl')
loaded_model = joblib.load(MODEL_PATH)

def predict(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_inputs = {
                'gender': 0 if data['gender'] == 'Male' else 1,
                'age': data['age'],
                'height': data['height'],
                'weight': data['weight'],
                'duration': data['duration'],
                'heart_rate': data['heart_rate'],
                'body_temp': data['body_temp']
            }
            input_df = pd.DataFrame(user_inputs, index=[0])
            
            prediction = loaded_model.predict(input_df)
            result = f"{prediction[0]:,.2f}" 

    else:
        form = PredictionForm()  

    return render(request, 'predict.html', {'form': form, 'result': result})
