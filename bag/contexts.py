from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Context processor for storing the bag data within the session.

    **Context**

    ``bag_items``
        A list of all instances of :model:`products.Product` in the bag.
    ``total``
        The sum total of all instances of :model:`products.Product.price`
        in the bag.
    ``product_count``
        The sum total of all instances of :model:`products.Product`
        in the bag.
    ``delivery``
        The calculated delivery cost.
    ``free_delivery_delta``
        The difference between FREE_DELIVERY_THRESHOLD & total where
        FREE_DELIVERY_THRESHOLD > total
    ``free_delivery_threshold``
    The threshold at which delivery becomes free
    ``grand_total``
    total + delivery

    **Template:**

    :template:`menu/menu.html`
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        subtotal = quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
