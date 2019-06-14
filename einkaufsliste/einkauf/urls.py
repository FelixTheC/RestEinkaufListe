from django.conf.urls.static import static
from django.urls import re_path

from einkaufsliste import settings
from . import views
from .views import ListBookings, ListProducts, UpdateProduct, DeleteProduct
from .views import CreateBookingEntry
from .views import CreateProduct

app_name = 'einkauf'
urlpatterns = [
      re_path(r'^$', ListBookings.as_view(), name='bookingList'),
      re_path(r'^products/$', ListProducts.as_view(), name='productList'),
      re_path(r'^create_product/$', CreateProduct.as_view(), name='createProduct'),
      re_path(r'^update_product/(?P<pk>[\d]+)/$', UpdateProduct.as_view(), name='updateProduct'),
      re_path(r'^delete_product/(?P<pk>[\d]+)/$', DeleteProduct.as_view(), name='deleteProduct'),
      re_path(r'^create_booking/$', CreateBookingEntry.as_view(), name='createBooking'),
      re_path(r'^mark_booking_buyed/(?P<pk>[\d]+)/$', views.markBookingEntryBuyed, name='markBooking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)