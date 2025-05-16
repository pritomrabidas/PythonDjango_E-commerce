from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Slider
from account.models import CustomUser
@login_required(login_url='login')
# @login_required(login_url='reg')

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
