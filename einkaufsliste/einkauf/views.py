from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView

from .models import Product
from .models import Booking


@method_decorator(csrf_exempt, name='dispatch')
class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('einkauf:createBooking')

    def get_context_data(self, **kwargs):
        context = super(CreateProduct, self).get_context_data(**kwargs)
        context['form_title'] = 'Create Product'
        return context

    def form_valid(self, form):
        return super(CreateProduct, self).form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('einkauf:bookingList')

    def get_context_data(self, **kwargs):
        context = super(UpdateProduct, self).get_context_data(**kwargs)
        context['form_title'] = 'Update Product'
        return context

    def form_valid(self, form):
        return super(UpdateProduct, self).form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class CreateBookingEntry(CreateView):
    model = Booking
    fields = ['product', ]
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('einkauf:bookingList')

    def get_context_data(self, **kwargs):
        context = super(CreateBookingEntry, self).get_context_data(**kwargs)
        context['form_title'] = 'Create new entry'
        context['productform'] = True
        return context

    def form_valid(self, form):
        return super(CreateBookingEntry, self).form_valid(form)


class ListBookings(ListView):
    model = Booking
    queryset = Booking.objects.filter(purchased=False)
    template_name = 'list.html'


@csrf_exempt
def markBookingEntryBuyed(request, pk):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, pk=pk)
        booking.purchased = True
        booking.save()
        return HttpResponse(200)
    else:
        return HttpResponse(404)