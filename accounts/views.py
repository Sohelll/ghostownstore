from django.shortcuts import render, redirect
from .models import UserProfileInfo, User
from django.contrib import messages, auth

def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # GET form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        address = request.POST['address']
        phone_num = request.POST['ph_num']
        phone_num2 = request.POST['ph_num_2']

        if password == password2:
            # checking if username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'this username is already present')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email address already present')
                    return redirect('register')
                else:
                    #looks good
                    user = User.objects.create(username=username, password=password, email=email,
                                               first_name=first_name, last_name=last_name) 
                    user.save()

                    #adding the profile fields on Userinfo model

                    profile = UserProfileInfo.objects.create(
                        address=address, phone_num=phone_num, phone_num_2=phone_num2, user=user)
                    
                    print('before img')
                    if 'profile_pic' in request.FILES:
                        profile.profile_pic = request.FILES['profile_pic']

                    profile.save()

                    messages.success(
                        request, 'You are now registered and CAN login in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'pages/dashboard.html')
