from django.conf.urls import url
from django.conf.urls.static import static
from einkaufsliste import settings
from . import views
from .views import ListBookings, ListProducts, UpdateProduct, DeleteProduct
from .views import CreateBookingEntry
from .views import CreateProduct

app_name = 'einkauf'
urlpatterns = [
      url(r'^$', ListBookings.as_view(), name='bookingList'),
      url(r'^products/$', ListProducts.as_view(), name='productList'),
      url(r'^create_product/$', CreateProduct.as_view(), name='createProduct'),
      url(r'^update_product/(?P<pk>[\d]+)/$', UpdateProduct.as_view(), name='updateProduct'),
      url(r'^delete_product/(?P<pk>[\d]+)/$', DeleteProduct.as_view(), name='deleteProduct'),
      url(r'^create_booking/$', CreateBookingEntry.as_view(), name='createBooking'),
      url(r'^mark_booking_buyed/(?P<pk>[\d]+)/$', views.markBookingEntryBuyed, name='markBooking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)