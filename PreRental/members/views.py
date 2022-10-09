from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get['first_name']
            surname = form.cleaned_data.get['last_name']
            email = form.cleaned_data.get['email']
            password = form.cleaned_data.get['password']
            user = authenticate(request, name=name, surname=surname, email=email, password=password)
            login(request, user)
            messages.success(request, ('New Account Created: ' + name +"!"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "authenticate/register.html", 
        {'form': form}
        )

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('home')
        else:
            messages.error(request, ('Error Logging In - Please Try Again...'))
            return redirect('login')
    return render(request, "authenticate/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out...'))
    return redirect('home')


# Create your views here.
