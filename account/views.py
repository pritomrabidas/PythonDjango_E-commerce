from django.shortcuts import render , redirect ,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.contrib import messages
import random

def reg(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in.")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zipcode = request.POST.get('zipcode')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            otp = random.randint(1000, 9999)
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, country=country, zipcode=zipcode, image=image, password=password ,otp=otp)
            user.save()
            send_registration_email(email,otp)
            return redirect('verify_otp')
        else:
            messages.error(request, "Passwords do not match.")
        
    return render(request, 'auth/registration.html')

def send_registration_email(email,otp):
    try:
        subject = 'Welcome to Our Site'
        message = f'Thank you for registering with us. Your OTP is {otp} .'
        from_email = settings.EMAIL_HOST_USER 
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print("Email sending failed:", e)


def verify_otp(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp:
            user = CustomUser.objects.filter(otp=otp).first()
            if user:
                user.is_verified = True
                user.save()
                return redirect('login')
        else:
            return redirect('verify_otp')
        
    return render(request, 'auth/otp_submit.html')

def logout(request):
    auth_logout(request)
    return redirect('reg')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_verified:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'auth/login.html', {'error': 'Your account is not verified yet.'})
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')

def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            otp = random.randint(1000, 9999)
            user.otp = otp
            user.save()
            send_registration_email(email, otp)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request, 'auth/forget.html')

def forget_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp:
            user = CustomUser.objects.filter(otp=otp).first()
            if user:
                user.is_verified = True
                user.save()
                return redirect('forget_pass')
            else:
                messages.error(request, "Invalid OTP.")
        else:
            messages.error(request, "Please enter the OTP.")
    return redirect('forget')

def forget_pass(request):
    if request.method == 'POST':
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        user = CustomUser.objects.filter(is_verified=True).first()
        if user:
            if pass1 == pass2:
                user.set_password(pass1)
                user.save()
                return redirect('home')
            else:
                messages.error(request, "Passwords do not match.")      
                    
    return render(request, 'auth/forget_pass.html')


@login_required(login_url='login')
def update(request,id):
    update = request.user
    User = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zipcode = request.POST.get('zipcode')
        image = request.FILES.get('image')
        if username:
            User.username = username
        
        User.email = email
        User.phone = phone
        User.city = city
        User.state = state
        User.country = country
        User.zipcode = zipcode
        if image:
            User.image = image
        
        User.save()
        return redirect('home')
    return render(request, 'home/my_account.html',{'update': User})
