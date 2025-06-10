from django.shortcuts import render, redirect
from django.http import HttpRequest
from tours.models import Tour

def overview(request: HttpRequest):
    cart_items = request.session.get('cart_items', [])
    tours = Tour.objects.filter(id__in=cart_items)
    total_price = sum(tour.tour_price for tour in tours)

    return render(request, 'cart/overview.html', {
        'cart_items': tours,
        'cart_count': len(cart_items),
        'total_price': total_price
    })

def add_to_cart(request, tour_id):
    cart_items = request.session.get('cart_items', [])
    if tour_id not in cart_items:
        cart_items.append(tour_id)
        request.session['cart_items'] = cart_items
    return redirect('cart:overview')

def remove_from_cart(request, tour_id):
    cart_items = request.session.get('cart_items', [])
    if tour_id in cart_items:
        cart_items.remove(tour_id)
        request.session['cart_items'] = cart_items
    return redirect('cart:overview')

def clear_cart(request):
    request.session['cart_items'] = []
    return redirect('cart:overview')
