from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping bag currently")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IoUabH1NiUB2nD2ziD1tSUlOKGyCLFdjFXxcOPNDxQx5kKt7GZG4DnOmwH8nr7J3By7FIjfWGNz3d5xUxFqTV7400EKIFE9aM',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
