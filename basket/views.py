from django.shortcuts import render


def view_basket(request):
    """ A view that renders the basket contents """

    return render(request, 'basket/basket.html')
