from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ia8FbFf2QgfqgMTzHH2RgWNbvIDKZlIoKU0Yb8Iv3uLQcl06RnfIg1118YAIjbHLf7E48Pxa7wz07j62oAmxUvO00KVWwb8m2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
