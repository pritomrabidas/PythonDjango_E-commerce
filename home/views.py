from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Product, Slider
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
from django.contrib import messages


@login_required(login_url='login')

def home(request):
    sliders = Slider.objects.all()
    new_arrival = Product.objects.filter(new_arrival=True)
    top_rated = Product.objects.filter(top_rated=True)
    featured = Product.objects.filter(featured=True)
    return render(request, 'home/home.html', {'sli': sliders,'new_arrival': new_arrival, 'top_rated': top_rated, 'featured': featured})

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

def shop(request):
    products = Product.objects.all()
    return render(request, 'home/shop.html', {'pro': products})

def singleProduct(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'home/singleProduct.html', {'pro': product})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=request.user, product=product)
        cart.quantity += 1
        cart.save()
    except Cart.DoesNotExist:
        cart = Cart.objects.create(product=product, user=request.user, quantity=1)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def some_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'template.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    return render(request, 'home/checkout.html')