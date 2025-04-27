from django.shortcuts import render
from django.core.mail import send_mail
from .models import costom_user
from django.contrib.auth import authenticate, login 

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
        zip_code = request.POST.get('zip_code')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = costom_user.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, country=country, zip_code=zip_code, image=image, password=password)
            user.save()
    return render(request, 'auth/login.html')