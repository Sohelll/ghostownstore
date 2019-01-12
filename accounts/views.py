from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'pages/dashboard.html')
