#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.06.19
@author: felix
"""
from django.test import TestCase, Client

from einkauf.models import Product, Categorie, Booking


class ViewTests(TestCase):

    fixtures = ['data.yaml']

    client = Client()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_empty_booking_overview(self):
        prods = Product.objects.all()
        response = self.client.get('/api/', follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        for prod in prods:
            self.assertNotContains(response, prod.name)
        self.assertContains(response, 'Create new entry')
        self.assertContains(response, 'Einkaufsliste')
        self.assertContains(response, 'Refresh list')

    def test_get_create_new_booking_entry(self):
        response = self.client.get('/api/create_booking/', follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        prods = Product.objects.all()
        cats = Categorie.objects.all()
        for prod in prods:
            self.assertContains(response, prod.name)
        for cat in cats:
            self.assertContains(response, cat.name)
        self.assertContains(response, 'Eintragen')
        self.assertContains(response, 'Back')
        self.assertContains(response, 'Create new product')

    def test_post_new_booking_entry(self):
        prods = Product.objects.all()[:5]
        data = {
            'product': list([i.pk for i in prods])
        }
        response = self.client.post('/api/create_booking/', follow=True, data=data, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        booking = Booking.objects.all()
        self.assertEqual(booking.count(), 5)
        for prod in prods:
            self.assertContains(response, prod.name)
