from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Product, Categorie
from .models import Booking
from .forms import BookingForm


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
        return reverse('einkauf:productList')

    def get_context_data(self, **kwargs):
        context = super(UpdateProduct, self).get_context_data(**kwargs)
        context['form_title'] = 'Update Product'
        return context

    def form_valid(self, form):
        return super(UpdateProduct, self).form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('einkauf:productList')


@method_decorator(csrf_exempt, name='dispatch')
class CreateBookingEntry(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'select_item_form.html'

    def get_success_url(self):
        return reverse('einkauf:bookingList')

    def get_context_data(self, **kwargs):
        context = super(CreateBookingEntry, self).get_context_data(**kwargs)
        context['form_title'] = 'Create new entry'
        context['products'] = Product.objects.all().order_by('name')
        context['categorie'] = Categorie.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            for prod in request.POST.getlist('product'):
                try:
                    booking = Booking()
                    booking.purchased = False
                    booking.product = Product.objects.get(pk=prod)
                    booking.save()
                except ValueError:
                    pass
            return redirect(self.get_success_url())
        else:
            return redirect(self.get_success_url())


class ListBookings(ListView):
    model = Booking
    queryset = Booking.objects.filter(purchased=False)
    template_name = 'list.html'


class ListProducts(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'listProducts.html'


@csrf_exempt
def markBookingEntryBuyed(request, pk):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, pk=pk)
        booking.purchased = True
        booking.save()
        return HttpResponse(200)
    else:
        return HttpResponse(404)