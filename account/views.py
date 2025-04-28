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
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, country=country, zipcode=zipcode, image=image, password=password)
            user.save()
            send_registration_email(email)
            return redirect('login')
    return render(request, 'auth/login.html')

def send_registration_email(email):
    otp = random.randint(0000, 9999)
    subject = 'Welcome to Our Site'
    message = f'Thank you for registering with us your otp is {otp}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]  
    if isinstance(recipient_list, list) or isinstance(recipient_list, tuple):
        send_mail(subject, message, from_email, recipient_list)
    else:
        raise ValueError("Recipient list must be a list or tuple.")
