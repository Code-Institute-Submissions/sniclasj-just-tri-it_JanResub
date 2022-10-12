from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('listings'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ls0VJFjb6q15IqHdY57QdcrpRIuuBBISwUG9tjafr1OwJNMzl4eSPnPGyHmsx2rYQjMT2ZJxuhMMUYQdf6S1u7U00Uf1744v6',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
