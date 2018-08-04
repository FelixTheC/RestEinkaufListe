from django.conf.urls import url
from django.conf.urls.static import static
from einkaufsliste import settings
from . import views
from .views import ListBookings
from .views import CreateBookingEntry
from .views import CreateProduct

app_name = 'einkauf'
urlpatterns = [
    url(r'^$', ListBookings.as_view(), name='bookingList'),
    url(r'^create_product/$', CreateProduct.as_view(), name='createProduct'),
    url(r'^create_booking/$', CreateBookingEntry.as_view(), name='createBooking'),
    url(r'^mark_booking_buyed/(?P<pk>[\d]+)/$', views.markBookingEntryBuyed, name='markBooking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)