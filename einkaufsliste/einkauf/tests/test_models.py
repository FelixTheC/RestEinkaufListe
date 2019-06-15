from django.test import TestCase
from einkauf.models import Categorie, Booking
from einkauf.models import Product


class CategorieModelTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_new_categorie(self):
        cat = Categorie.objects.create(name='Test', description='foo_bar')
        self.assertIsNotNone(cat)
        self.assertEqual(cat.name, 'Test')
        self.assertEqual(cat.description, 'foo_bar')
        self.assertEqual(str(cat), 'Test')

    def test_create_new_categorie_without_description(self):
        cat = Categorie.objects.create(name='Test')
        self.assertIsNotNone(cat)
        self.assertEqual(cat.name, 'Test')
        self.assertIsNone(cat.description)
        self.assertEqual(str(cat), 'Test')


class ProductModelTest(TestCase):

    fixtures = ['data.yaml']

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_new_prodcut_success(self):
        cat = Categorie.objects.get(pk=1)
        prod = Product.objects.create(name='Foo', description='bar', categorie=cat)
        self.assertIsNotNone(prod)
        self.assertEqual(prod.name, 'Foo')
        self.assertEqual(prod.description, 'bar')
        self.assertEqual(prod.categorie_id, cat.pk)
        self.assertIsNotNone(prod.created_at)

    def test_create_new_product_success_without_categorie(self):
        prod = Product.objects.create(name='Foo', description='bar')
        self.assertIsNotNone(prod)
        self.assertEqual(prod.categorie_id, 1)


class BookingModelTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_booking(self):
        cat = Categorie.objects.create(name='Test', description='foo_bar')
        prod = Product.objects.create(name='Foo', description='bar', categorie=cat)
        booking = Booking.objects.create(product=prod)
        self.assertIsNotNone(booking)
        self.assertEqual(booking.product, prod)
        self.assertEqual(booking.purchased, False)
        self.assertIsNotNone(booking.created_at)
