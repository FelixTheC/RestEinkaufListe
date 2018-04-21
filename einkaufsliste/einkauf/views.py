from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser

from .models import Product
from .models import Booking


# Create your views here.
def create_product(request, name, description):
    try:
        product = Product.objects.get(name=name)
    except ObjectDoesNotExist:
        pass

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        print(request)
        return HttpResponse(status=200)