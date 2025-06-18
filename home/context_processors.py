from .models import Cart

def cart_items_processor(request):
    cart_items = Cart.objects.filter(user=request.user.username)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return {'cart_items': cart_items, 'total_price': total_price}
