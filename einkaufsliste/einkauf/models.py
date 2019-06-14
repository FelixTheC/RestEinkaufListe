from django.db import models
from datetime import datetime

from django.urls import reverse


class Categorie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey(Categorie, default=1, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=datetime.today(), blank=True, editable=False)

    def __str__(self):
        if self.description:
            return self.name + '-' + self.description
        else:
            return self.name

    def get_update_view(self):
        return reverse('einkauf:updateProduct', kwargs={
            'pk': self.pk,
        })

    def get_delete_view(self):
        return reverse('einkauf:deleteProduct', kwargs={
            'pk': self.pk,
        })


class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.today(), blank=True, editable=False)

    def __str__(self):
        return self.product.name + '-' + str(self.purchased)