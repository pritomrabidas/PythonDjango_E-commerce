from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .models import CustomUser
from django.contrib.auth import authenticate, login 
from django.conf import settings
import random
def login(request):
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
    return render(request, 'auth/login.html')

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

# def logout(request):
#     logout(request)
#     return redirect('login')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('name')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'auth/login.html')