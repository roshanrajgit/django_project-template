from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import user_list
# Create your views here.

def login(request):
    if request.method == 'POST':
        username =(request.POST['username'])
        password =(request.POST['password'])
        #user = auth(is_authenticate.username==username, is_authenticate.password==password )
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
                #redirect to success page
            else:
                messages.info(request,"User is inactive")
        else:
            messages.info(request,"Invalid creditatials")
            return render(request, 'login.html')
    else:
        return render (request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name =(request.POST['first_name'])
        last_name =(request.POST['last_name'])
        username =(request.POST['username'])
        email =(request.POST['email'])
        password1 =(request.POST['password1'])
        password2 =(request.POST['password2'])

        if password1==password2:
            if User.objects.filter(username= username).exists():
                messages.info(request,'User name already taken')
                #return redirect('register')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                #return redirect('register')
                return render(request,'register.html')
            else:
                user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                return redirect('login')
                
                
            
        else:
            print ('Both password not same')
            #return redirect('/')
            return render(request,'register.html')
        return redirect('/')
        
    else:
        return render (request,'register.html')


def user_list(request):
    usrs = User.objects.all()

    return render (request,'user_list.html',{'usrs':usrs})

def logout(request):
    
    auth.logout(request)
    return redirect('/')

