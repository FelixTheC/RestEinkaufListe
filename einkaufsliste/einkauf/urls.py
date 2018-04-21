from django.conf.urls import url
from einkauf import views

app_name = 'einkauf'
urlpatterns = [
    url(r'^create_product/(?P<name>[/D]+/(?P<description>[/D]+/$))', views.create_product, name='createProduct')
]