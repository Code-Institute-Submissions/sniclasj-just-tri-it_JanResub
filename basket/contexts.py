from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from listings.models import Listing


def basket_contents(request):

    basket_items = []
    total = 0
    listing_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        listing = get_object_or_404(Listing, pk=item_id)
        total += quantity * listing.price
        listing_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'listing': listing,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'listing_count': listing_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
