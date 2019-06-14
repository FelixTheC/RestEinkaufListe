from django.contrib import admin
from .models import Product
from .models import Booking
from .models import Categorie

# Register your models here.
admin.site.register(Product)
admin.site.register(Booking)
admin.site.register(Categorie)
