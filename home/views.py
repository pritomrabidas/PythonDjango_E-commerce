from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Slider
from account.models import CustomUser
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
from django.contrib import messages


@login_required(login_url='login')

def home(request):
    sliders = Slider.objects.all()
    return render(request, 'home/home.html', {'sli': sliders})

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


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"Message from {name} <{email}>:\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully!')
        except BadHeaderError:
            messages.error(request, 'Invalid header found.')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

        return redirect('contact')
    return render(request, 'home/contact.html')
