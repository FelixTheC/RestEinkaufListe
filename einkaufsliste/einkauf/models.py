from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.today(), blank=True, editable=False)

    def __str__(self):
        if self.description:
            return self.name + '-' + self.description
        else:
            return self.name


class Booking(models.Model):
    product = models.ForeignKey(Product)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.today(), blank=True, editable=False)

    def __str__(self):
        return self.product.name + '-' + str(self.purchased)