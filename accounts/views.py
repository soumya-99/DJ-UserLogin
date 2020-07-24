from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request, 'Username taken!!')
                # print("Username taken!!")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email Already Exists!!')
                # print("Email Already Exists!!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                # messages.info(request, 'User Created Successfully!!!!!!')
                # print('User Created Successfully!!!!!!')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!!')
            # print("Password not matching!!")
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')